# test_jar.py
# Kelis Hightower

# imprts the jar class from the jar file
from jar import Jar

# tetsing the init function


def test_init():
    jar = Jar(4)  # creates jar with a capacity of 4
    assert jar.capacity == 4  # checks to see if 4 is retuned when the cpacity func is called
    assert jar.size == 0  # sets jar size to 0
    jar1 = Jar()  # created a new jar with the defualt capcity (12)
    assert jar1.capacity == 12  # checks ot make sure the new jar indeed printed out the deafult capcity

# test the string functions in the class


def test_str():
    jar = Jar()  # creates new jar with default values
    assert str(jar) == ""  # checks if the starting string is empty
    jar.deposit(1)  # adds one cookie to the jar
    assert str(jar) == "🍪"  # checks to make sure one cookie in prinited out to represent the capacity
    jar.deposit(11)  # adds 11 cookies
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"  # checks to make sue the value of capcity updated as intended

# tets the depoti function


def test_deposit():
    jar = Jar()  # creates a new jar with the defult vlaues
    jar.deposit(4)  # adds 4 cookies to jar
    assert jar.size == 4  # make sure the size value updated to 4 with the new deposit
    jar.deposit(4)  # adds 4 more
    assert jar.size == 8  # make sure that its is now addd the 4 to the OG 4
    jar.deposit(4)  # adds 4 more
    assert jar.size == 12  # make sure it updates accorningly to 12 (4+4+4 = 12)


# test the withdraw function
def test_withdraw():
    jar = Jar()  # sets a new jar with the default values
    jar.deposit(12)  # adds 12 cookies
    jar.withdraw(4)  # takes away 4 cookies
    assert jar.size == 8  # makes sure the funtiin can do subtraction and additon to result in 8
    jar.withdraw(4)  # takes out 4 more
    assert jar.size == 4  # should update to 4
    jar.withdraw(4)  # takes out 4 more
    assert jar.size == 0  # the jar size should now have no cookies in it
