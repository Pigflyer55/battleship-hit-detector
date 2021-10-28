class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def x(self):
        return self.x()

    def y(self):
        return self.y()

    def set(self, other):
        if type(other) == Coordinate:
            self.x = other.x
            self.y = other.y
        else:
            raise AttributeError("Object " + other + " is not a Coordinate!")
