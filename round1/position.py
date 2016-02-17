import math

class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_distance(self, x: int, y: int) -> int:
        return get_distance(self.x, self.y, x, y)

def get_distance(x1: int, x2: int, y1: int, y2: int) -> int:
    return math.ceil(math.sqrt(math.pow(abs(x1 - x2), 2) + math.pow(abs(y1 - y2), 2)))
