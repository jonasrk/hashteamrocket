result = []

def printLoad(drone, warehouse, product, count):
    result.append("%d L %d %d %d" % (drone, warehouse, product, count))
    
def printDeliver(drone, customer, product, count):
    result.append("%d D %d %d %d" % (drone, customer, product, count))

def printToFile(file_name):
    f = open("result/" + file_name, "w+")
    print(len(result))
    f.write("%d\n" % len(result))
    for line in result:
        print(line)
        f.write(line + "\n")