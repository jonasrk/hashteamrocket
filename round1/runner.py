import math

from drone import Drone, get_distance
from tr_parser import Parser
from tr_printer import Printer

class Runner:
    def __init__(self, file_name: str):
        self.printer = Printer(file_name)
        self.parser = Parser(file_name)
        deadline, drones, product_weights, warehouses, orders = self.parser.parse_file()
        self.deadline = deadline
        self.drones = drones
        self.product_weights = product_weights
        self.warehouses = warehouses
        self.orders = orders

    def run_input(self) -> None:
        turn = 0
        while turn < self.deadline:
            for drone in self.drones:
                drone.tick(turn)
                if drone.busy:
                    continue
                ordered_warehouses = self.get_ordered_warehouses(drone)
                ordered_orders = self.get_ordered_orders(drone, ordered_warehouses[0].x, ordered_warehouses[0].y)
                if len(ordered_orders) > 0:
                    order = ordered_orders[0]
                    order.completed = True
                    free_at = turn
                    for warehouse in ordered_warehouses:
                        for product_name, count in enumerate(order.product_counts):
                            if warehouse.product_counts[product_name] > 0 and count > 0:
                                available_product_count = warehouse.product_counts[product_name]
                                available_load_count = math.floor(drone.capacity / self.product_weights[product_name])
                                load_count = min(count, available_product_count, available_load_count)
                                warehouse.product_counts[product_name] -= load_count
                                count -= load_count
                                drone.capacity -= self.product_weights[product_name] * load_count
                                if load_count > 0:
                                    free_at = drone.load_at(warehouse.x, warehouse.y, product_name, load_count, free_at)
                                    if free_at < self.deadline:
                                        self.printer.print_load(drone.name, warehouse.name, product_name, load_count)
                                if count > 0:
                                    free_at = self.unload_drone(drone, order.x, order.y, order.name, free_at)
                    if drone.capacity < drone.max_load:
                        free_at = self.unload_drone(drone, order.x, order.y, order.name, free_at)
            turn += 1
        self.printer.flush(True)

    def get_ordered_warehouses(self, drone: Drone):
        if len(self.warehouses) == 1:
            return self.warehouses
        ordered_warehouses = [(w, get_distance(w.x, drone.x, w.y, drone.y)) for w in self.warehouses]
        ordered_warehouses.sort(key=lambda d: d[1])
        return [ordered_warehouse[0] for ordered_warehouse in ordered_warehouses]

    def get_ordered_orders(self, drone: Drone, x: int, y: int):
        ordered_orders = []
        for order in self.orders:
            if not order.completed:
                weight = 0
                for i, product_count in enumerate(order.product_counts):
                    weight += self.product_weights[i] * product_count
                distance = drone.get_distance(order.x, order.y)
                ordered_orders.append((order, distance * math.ceil(weight / drone.max_load) + distance))
        ordered_orders.sort(key=lambda d: d[1])
        return [ordered_order[0] for ordered_order in ordered_orders]

    def unload_drone(self, drone: Drone, x: int, y: int, order_name: int, free_at: int) -> int:
        free_at = drone.deliver_to(x, y, free_at)
        if free_at < self.deadline:
            for product_name in drone.loaded_products:
                self.printer.print_deliver(drone.name, order_name, product_name, drone.loaded_products[product_name])
            drone.loaded_products = {}
        return free_at

if __name__ == '__main__':
    for file in ["busy_day"]:
        #, "mother_of_all_warehouses", "redundancy"
        runner = Runner(file)
        runner.run_input()
