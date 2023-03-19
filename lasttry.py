class Ren:
    def __init__ (self, x, y, z, e, q):
        self.x = x
        self.y = y
        self.z = z
        self.e = e
        self.q = q

    def add(self, other):
        return Ren(self.x + other.x, self.y + other.y, self.z + other.z, self.e + other.e, self.q + other.q)

    def subtract(self, other):
        return Ren(self.x - other.x, self.y - other.y, self.z - other.z, self.e - other.e, self.q - other.q)

    def multiply(self, scalar):
        return Ren(self.x * scalar, self.y * scalar, self.z * scalar, self.e * scalar, self.q * scalar)

    def __str__(self):
        return f"({self.x},{self.y},{self.z},{self.e},{self.q})"


if __name__ == "__main__":
    v1 = Ren(2, 2, 3, 5, 7)
    v2 = Ren(5, 3, 7, 1, 4)
    number = 2

    print(v1.add(v2))
    print(v1.subtract(v2))
    print(v1.multiply(number))