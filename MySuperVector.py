class SuperVector:
    def __init__(self, x, y, x):
        self.x = 5
        self.y = 2
        self.z = 7
    
    def add(self, other):
        return SuperVector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def subtract(self, other):
        return SuperVector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def multiply(self, scalar):
        return SuperVector(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"