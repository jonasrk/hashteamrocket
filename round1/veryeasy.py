from round1.dron import Drone
from round1.parse import parse_file
from round1.printer import printLoad, printDeliver, printToFile


n_rows, n_cols, n_drones, deadline, max_load, p, products, warehouse, warehouses, o, orders = parse_file('data/redundancy.in')

drone = Drone(warehouses[0]["cords"][0], warehouses[0]["cords"][1])
current_oder = 0
turn = 0
while turn < deadline and current_oder < len(orders):
    order = orders[current_oder]
    for product, count in enumerate(order["products"]):
        for i, warehouse in enumerate(warehouses):
            if warehouse["products"][product] > 0 and count > 0:
                warehouse["products"][product] -= 1
                count -= 1
                turn = drone.to(warehouse["cords"][0], warehouse["cords"][1], turn)
                if (turn < deadline): 
                    printLoad(0, i, product, 1)
                turn = drone.to(order["cords"][0], order["cords"][1], turn)
                if (turn < deadline): 
                    printDeliver(0, current_oder, product, 1)
    current_oder += 1
        
printToFile("redundancy.out")