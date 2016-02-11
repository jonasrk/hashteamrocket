import math


class Drone:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def to(self, x, y, turn):
        self.free_at = turn + math.ceil(math.sqrt(math.pow(abs(self.x - x), 2) + math.pow(abs(self.y - y), 2))) + 1
        self.x = x
        self.y = y
        return self.free_at