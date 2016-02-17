from drone import Drone
from order import Order
from warehouse import Warehouse

class Parser:
    def __init__(self, file_name):
        self.file_name = "round1/data/" + file_name + ".in"

    def parse_file(self):
        with open(self.file_name, 'r') as file:
            _, _, n_drones, deadline, max_load = [int(x) for x in file.readline().split()]
            product_count = int(file.readline())
            product_weights = [int(product_weight) for product_weight in file.readline().split()]
            warehouses = []
            warehouse_count =int(file.readline())
            for i in range(warehouse_count):
                coordinates = [int(x) for x in file.readline().split()]
                product_counts = [int(x) for x in file.readline().split()]
                warehouses.append(Warehouse(i, *coordinates, product_counts=product_counts))
            orders = []
            order_count = int(file.readline())
            for i in range(order_count):
                coordinates = [int(x) for x in file.readline().split()]
                order_product_count = int(file.readline())
                product_counts = [0] * product_count
                for order_product in file.readline().split():
                    product_counts[int(order_product)] += 1
                orders.append(Order(i, *coordinates, product_counts=product_counts))
            drones = create_drones(n_drones, max_load, warehouses[0].x, warehouses[0].y)
        return (deadline, drones, product_weights, warehouses, orders)

def create_drones(n_drones: int, max_load: int, x: int, y: int):
    drones = []
    for drone_name in range(n_drones):
        drones.append(Drone(drone_name, max_load, x, y))
    return drones
