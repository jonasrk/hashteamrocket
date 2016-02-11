from round1.dron import Drone
from round1.parse import parse_file
from round1.printer import printLoad, printDeliver, printToFile


n_rows, n_cols, n_drones, deadline, max_load, p, products, warehouse, warehouses, o, orders = parse_file('data/test.in')

drone = Drone(warehouses[0]["cords"][0], warehouses[0]["cords"][1])
current_oder = 0
turn = 0
while turn < deadline:
    order = orders[current_oder]
    current_oder += 1
    for product, count in enumerate(order["products"]):
        weight = max_load
        while count > 0 and weight > 0:
            # Fly to different one
            for i, warehouse in enumerate(warehouses):
                if warehouse["products"][product] > 0:
                    load = min(warehouse["products"][product], count, max_load / products[product])
                    weight -= load * products[product]
                    if load > 0:
                        printLoad(0, i, product, count)
                        turn += 1
                        count -= load
                        warehouse["products"][product] -= load
                        turn = drone.to(warehouse["cords"][0], warehouse["cords"][1], turn)
    if load > 0:
        printDeliver(0, current_oder, product, load)
        turn += 1
        turn = drone.to(order["cords"][0], order["cords"][1], turn)
        
printToFile("busy_day.out")