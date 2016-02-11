import math


class Drone:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isFree = True
        
    def tick(self, turn):
        if self.isFree:
            return True
        self.isFree = turn == self.free_at
        return self.isFree
    
    def isIdle(self):
        return self.isFree
    
    def to(self, x, y, turn):
        self.free_at = turn + math.ceil(math.sqrt(math.pow(abs(self.x - x), 2) + math.pow(abs(self.y - y), 2))) + 1
        self.x = x
        self.y = y
        self.isFree = False
        return self.free_at