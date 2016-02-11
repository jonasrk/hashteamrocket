from round1.dron import Drone
from round1.parse import parse_file
from round1.printer import printLoad, printDeliver, printToFile


n_rows, n_cols, n_drones, deadline, max_load, p, products, warehouse, warehouses, o, orders = parse_file('data/busy_day.in')

drones = []
for d in range(n_drones):
    drones.append(Drone(warehouses[0]["cords"][0], warehouses[0]["cords"][1]))

current_oder = 0
turn = 0
while turn < deadline and current_oder < len(orders):
    for drone_i, drone in enumerate(drones):
        drone.tick(turn)
        if drone.isIdle():
            order = orders[current_oder]
            drone_free = turn
            for product, count in enumerate(order["products"]):
                for i, warehouse in enumerate(warehouses):
                    if warehouse["products"][product] > 0 and count > 0:
                        warehouse["products"][product] -= 1
                        count -= 1
                        drone_free = drone.to(warehouse["cords"][0], warehouse["cords"][1], drone_free)
                        if (drone_free < deadline): 
                            printLoad(drone_i, i, product, 1)
                        drone_free = drone.to(order["cords"][0], order["cords"][1], drone_free)
                        if (drone_free < deadline): 
                            printDeliver(drone_i, current_oder, product, 1)
            current_oder += 1
    turn += 1
        
printToFile("busy_day.out")