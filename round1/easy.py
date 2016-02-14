import math

from dron import Drone
from parse import parse_file
from printer import printLoad, printDeliver, printToFile


def doStuff(file_name):
    n_rows, n_cols, n_drones, deadline, max_load, p, products, warehouse_count, warehouses, o, orders = parse_file('data/' + file_name + '.in')
    
    drones = []
    for _ in range(n_drones):
        drones.append(Drone(warehouses[0]["cords"][0], warehouses[0]["cords"][1]))
    
    turn = 0
    while turn < deadline:
        for drone_i, drone in enumerate(drones):
            drone.tick(turn)
            if drone.isIdle():
                order = getBestOrder(orders, products, max_load, drone.x, drone.y)
                if order:
                    order["completed"] = True
                    drone_free = turn
                    for product, count in enumerate(order["products"]):
                        for _, warehouse in enumerate(getOrderedWarehouses(warehouses, drone.x, drone.y)):
                            if warehouse["products"][product] > 0 and count > 0:
                                load_count = min(count, warehouse["products"][product], math.floor(max_load / products[product]))
                                warehouse["products"][product] -= load_count
                                count -= load_count
        
#                                 total_weight = 0
#                                 load_count = 0
#         
#                                 # while order not fullfilled and drone not maxed out
#                                 while count != 0 and total_weight + products[product] <= max_load and warehouse["products"][product] > 0:
#                                     warehouse["products"][product] -= 1
#                                     count -= 1
#                                     load_count += 1
#                                     total_weight += products[product]
        
                                drone_free = drone.to(warehouse["cords"][0], warehouse["cords"][1], drone_free)
                                if (drone_free < deadline): 
                                    printLoad(drone_i, warehouse["id"], product, load_count)
                                drone_free = drone.to(order["cords"][0], order["cords"][1], drone_free)
                                if (drone_free < deadline): 
                                    printDeliver(drone_i, order["id"], product, load_count)
        turn += 1
        
    printToFile(file_name + ".out")
    
def getOrderedWarehouses(warehouses, x, y):
    orderedWarehouses = [(w, getDistance(w["cords"][0], x, w["cords"][1], y)) for w in warehouses]
    orderedWarehouses.sort(key=lambda d: d[1])
    return [orderedWarehouse[0] for orderedWarehouse in orderedWarehouses]

def getBestOrder(orders, products, max_load, x, y):
    orderedOrders = []
    for order in orders:
        if not order["completed"]:
            weight = 0
            for i, product_count in enumerate(order["products"]):
                weight += products[i] * product_count
            distance = getDistance(order["cords"][0], x, order["cords"][1], y)
            orderedOrders.append((order, distance * math.ceil(weight / max_load) + distance))
    orderedOrders.sort(key=lambda d: d[1])
    if len(orderedOrders):
        return orderedOrders[0][0]
    else:
        return False

def getDistance(x1, x2, y1, y2):
    return math.sqrt(math.pow(abs(x1 - x2), 2) + math.pow(abs(y1 - y2), 2))
    
# doStuff("busy_day")
# doStuff("mother_of_all_warehouses")
doStuff("redundancy")
