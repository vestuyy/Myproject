class SuperVector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        return SuperVector(self.x + other.x, self.y + other.y, self.z + other.z)

    def subtract(self, other):
        return SuperVector(self.x - other.x, self.y - other.y, self.z - other.z)

    def multiply(self, scalar):
        return SuperVector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


if __name__ == "__main__":
    v1 = SuperVector(1, 2, 3)
    v2 = SuperVector(4, 5, 6)
    number = 3

    print(v1.add(v2))
    print(v1.subtract(v2))
    print(v1.multiply(number))

