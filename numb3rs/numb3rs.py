# numb3rs.py
# Kelis Hightower

# imports so you can use regular expression
import re
# import sys to use sys exits
import sys


def main():
    # sets the users input to a varible called result
    result = validate(input("IPv4 Address: "))
    # if the result is valid prints result (true or false)
    if result:
        print(result)
    # it not a valid input simply exit the program
    else:
        sys.exit(1)


# validate function
def validate(ip):
    # if the input matches this pattern return true if not return false
    # Pattern break down...
    # 1- the number can be 25(0,1,2,3,4,5) = a range of 250-255 OR
    # it can be any number between 200 - 249 giving each number after two its own range OR
    # it can be any 100 number OR
    # it could be a teen/a single number by itself
    # repated 4 times giving each of the 4 numbers in the ip adress the same constraints
    if re.match(
        r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\."
        r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\."
        r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\."
        r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$",
        ip,
        re.IGNORECASE,
    ):
        return True
    else:
        return False


# calls the main function
if __name__ == "__main__":
    main()
