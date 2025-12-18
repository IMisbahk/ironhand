class Smoother:
    def __init__(self, alpha=0.2):
        self.Alpha = alpha
        self.LastX = None
        self.LastY = None

    def Apply(self, x, y):
        if self.LastX is None:
            self.LastX = x
            self.LastY = y
            return x, y

        sx = int(self.Alpha * x + (1 - self.Alpha) * self.LastX)
        sy = int(self.Alpha * y + (1 - self.Alpha) * self.LastY)

        self.LastX = sx
        self.LastY = sy

        return sx, sy
