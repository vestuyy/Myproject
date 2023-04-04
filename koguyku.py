class Uno:
    def __init__(self, list_of_numbers):

        self.list_of_numbers = list_of_numbers




    def __add__(self, other):

        if len(self.list_of_numbers) != len(other.list_of_numbers):
            print("LENGHT OF VECTORS MUST BE SAME!!!!")
            return

        result = []

        for i in range(len(self.list_of_numbers)):
            added_vector = self.list_of_numbers[i] + other.list_of_numbers[i]
            result.append(added_vector)

        return result

    def __sub__(self, other):

        if len(self.list_of_numbers) != len(other.list_of_numbers):
            print("LENGHT OF VECTORS MUST BE SAME!!!!")
            return

        result = []

        for i in range(len(self.list_of_numbers)):
            subtract_vector = self.list_of_numbers[i] - other.list_of_numbers[i]
            result.append(subtract_vector)

        return result

    def multiply(self, other):

        result = []

        for i in range(len(self.list_of_numbers)):
            mul_vector = self.list_of_numbers[i] * other.list_of_numbers[i]
            result.append(mul_vector)

        return result




if __name__ == "__main__":

    v1 = Uno([1, 2, 4])
    v2 = Uno([4, 5, 3 ])


    print(v1 + v2)
    print(v1 - v2)
    print(v1 * v2)