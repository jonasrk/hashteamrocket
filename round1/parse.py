def parse_file(file_name):
    with open(file_name, 'r') as f:
        n_rows, n_cols, n_drones, deadline, max_load = [int(x) for x in f.readline().split()]
        p = int(f.readline())
        p_weights = [int(x) for x in f.readline().split()]
        w = int(f.readline())
        ws = []
        for _ in range(w):
            w_cords = f.readline().split()
#             ws.append([
#                 (int(w_cords[0]), int(w_cords[1])),
#                 [int(x) for x in f.readline().split()]
#             ])
            ws.append({"cords": (int(w_cords[0]), int(w_cords[1])), "products": [int(x) for x in f.readline().split()]})
            
        o = int(f.readline())
        os = []
        for _ in range(o):
            o_cords = f.readline().split()
            order = {
                "cords": (int(o_cords[0]), int(o_cords[1])),
                "product_count": int(f.readline())
            }
            order_products = [0] * p
            for order_product in f.readline().split():
                order_products[int(order_product)] += 1
            order["products"] = order_products
            os.append(order)
            
    return (n_rows, n_cols, n_drones, deadline, max_load, p, p_weights, w, ws, o, os)

if __name__ == '__main__':
    n_rows, n_cols, n_drones, deadline, max_load, p, p_weights, w, ws, o, os = parse_file('data/test.in')
    print("Grid Dimension: %d x %d" % (n_rows, n_cols))
    print("%d Turns" % (deadline))
    print("%d Drones with %d capacity" % (p, max_load))
    print("%d Product types" % (p))
    for i, pi in enumerate(p_weights):
        print("  Product %d with weight %d" % (i, pi))
    print("%d Warehouses" % (w))
    for i, wi in enumerate(ws):
        print("  Warehouse %d at %d, %d" % (i, wi["cords"][0], wi["cords"][1]))
        for j, pj in enumerate(wi["products"]):
            print("    with %d units of product %d" % (pj, j))
    print("%d Orders" % (o))
    for i, oi in enumerate(os):
        print("  Order %d to %d, %d with %d items" % (i, oi["cords"][0], oi["cords"][1], oi["product_count"]))
        for j, pj in enumerate(oi["products"]):
            print("    with %d units of product %d" % (pj, j))
