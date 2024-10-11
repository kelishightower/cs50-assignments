# jar.py
# Kelis Hightower

# P.S I had a teeny bit of outside help from my dad

# creates a class called jar
class Jar:
    # creates a deafult jar object with a dafult capcity of 12
    def __init__(self, capacity=12):
        # if the capacity is negtive for some reaoson riase a value error
        if capacity < 0:
            raise ValueError
        # sets the capacity of the jar
        self._capacity = capacity
        # sets the size of the jar
        self._size = 0
    # defines a string to represent the jar

    def __str__(self):
        # reuns the same ammount of cookie emojies as there is size
        return "🍪" * self.size
    # A methos to deposti cookies into the jar

    def deposit(self, n):
        # checks to make sure the ammount of cookies added isnt greater than the capcity
        if n > self._capacity or n + self.size > self._capacity:
            # if it is raise a value error
            raise ValueError
        # adds cookies to jar (increase the numerical value of size by the amount of cookies added
        self._size += n

    # mathod to remove cookies form the jar
    def withdraw(self, n):
        # chekc to see if your taking more cookies out then there is avaible
        if n > self.size:
            # if so raise a value error
            raise ValueError
        # subtract the value of size by the ammount of cookies taken out
        self._size -= n
    # a prperty that gets the value of the capcity of the jar

    @property
    def capacity(self):
        # returns the capacity
        return self._capacity
    # a property that returns the value of the size of the jar

    @property
    def size(self):
        # returns current size
        return self._size
# sets a main function


def main():
    # makes a jar object with a capacity of 4
    jar = Jar(4)
    # adds five cookies into the jar
    jar.deposit(5)
    # prints out the capacity
    print(jar.capacity)
    # prints out the size
    print(jar.size)


# calls the main function
if __name__ == "__main__":
    main()
