from enum import Enum

class Vortex:
    def __init__(self, n = None, d = None, c = None, p = None, t = None):
        self.name = n
        self.data = d
        self.connection = []
        self.color = c
        self.parent = p
        self.time = t

    def __str__(self):
        return self.name


class VortexColor(Enum):
    BLACK = 0
    GRAY = 127
    WHITE = 255