import os

class Printer:
    def __init__(self, file_name: str):
        self.file_name = "round1/result/" + file_name + ".out"
        self.result = []

    def print_load(self, drone_name: int, warehouse_name: int, product_name: int, product_count: int) -> None:
        self.result.append("%d L %d %d %d" % (drone_name, warehouse_name, product_name, product_count))

    def print_deliver(self, drone_name: int, order_name: int, product_name: int, product_count: int) -> None:
        self.result.append("%d D %d %s %d" % (drone_name, order_name, product_name, product_count))

    def flush(self, print_to_console: bool=False) -> None:
        if not os.path.exists(os.path.dirname(self.file_name)):
            try:
                os.makedirs(os.path.dirname(self.file_name))
            except OSError as exc:
                raise
        with open(self.file_name, "w+") as file:
            if print_to_console:
                print(len(self.result))
            file.write("%d\n" % len(self.result))
            for line in self.result:
                if print_to_console:
                    print(line)
                file.write(line + "\n")
            self.result = []
