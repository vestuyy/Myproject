class Vector:
    def __init__(self, list_of_numbers):
        """dunder (double underscore methods)

        :param x:        :param y:
        :param z:
        """

        # Data
        self.list_of_numbers = list_of_numbers   # Field or attribute


    # A list of functions

    def __add__(self, other):    # DUNDER method DUOUBLE underscore method (MAGIC methods)
        """ This add function adds the current vector (self.list_of_numbers) to the vector that is given as an argument (other)

        :param other:
        :return:
        """
        # Check if two vectors are the same size.
        if len(self.list_of_numbers) != len(other.list_of_numbers):
            print("Hey, in order to add two vectors, the lenght of vectors MUST be the same!")
            return

        result = []  # an empty list
        #v1 = Vector([1, 2, 3])  # v1 is called object, Vector is a class.
        # v2 = Vector([4, 5, 6])

        for i in range(len(self.list_of_numbers)):   # iterates every element in the self.list_of_numbers vector
            added_vector = self.list_of_numbers[i] + other.list_of_numbers[i]    # adds 1+1, after 2+2, then
            result.append(added_vector)                          # stores the result to result list

        return result

    def __sub__(self, other):
        """ This subtract function subtracts the current vector (self.list_of_numbers) to the vector that is given as an argument (other)

        :param other:
        :return: the result of subtract
        """
        # Check if two vectors are the same size.
        if len(self.list_of_numbers) != len(other.list_of_numbers):
            print("Hey, in order to subtract two vectors, the lenght of vectors MUST be the same!")
            return


        result = []  # an empty list
        #v1 = Vector([1, 2, 3])  # v1 is called object, Vector is a class.
        # v2 = Vector([4, 5, 6])

        for i in range(len(self.list_of_numbers)):   # iterates every element in the self.list_of_numbers vector
            subtract_vector = self.list_of_numbers[i] - other.list_of_numbers[i]    # adds 1+1, after 2+2, then
            result.append(subtract_vector)                          # stores the result to result list

        return result


    def multiply(self, number):
        """ This multiply  function does multiply the given vector with a scalar (number)

            vector = [1, 3, 5]
            k = 2

            Result
                   [2, 6, 10]

        :param other:
        :return: a vector
        """

        result = []  # an empty list
        #v1 = Vector([1, 2, 3])  # v1 is called object, Vector is a class.
        # v2 = Vector([4, 5, 6])

        for i in range(len(self.list_of_numbers)):   # iterates every element in the self.list_of_numbers vector
            mul_vector = self.list_of_numbers[i]*number
            result.append(mul_vector)                          # stores the result to result list

        return result


        # v1 = Vector([1, 2, 3])
        # v2 = Vector([4, 5, 6])
        # mul = 1*4 + 2*5 + 3*6  = 32


if __name__ == "__main__":

    # v1 is an Object or Instance
    v1 = Vector([1, 2 ])  #v1 is called object, Vector is a class.
    v2 = Vector([4, 5 ])

    print(v1 + v2)
    print(v1 - v2)