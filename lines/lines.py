# lines.py
# Kelis Hightower

# this allows us to use the comman line as a way to talk to our program
import sys

# checks the number of command-line arguments
# more than 2 exit and say to many and vise versa if less than 2
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# checks to see if the file has a .py extension if not say this isnt a python file and exit the program
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

try:
    # opens the file the user inputed and sets the file as a reading file "r"
    with open(sys.argv[1], "r") as file:
        # set the intital count to 0
        count = 0
        # go through each line in the file
        for line in file:
            # checks to make sure  the line is not blank or starts with a "#" (blank or commented line)
            if line.lstrip() != "" and not line.lstrip().startswith("#"):
                # if its not increase the count by one
                count += 1
        # print the value of count
        print(count)

# if the file dosent exsist or is not a valdi file exit and tell th user what went wrong 
except FileNotFoundError:
    sys.exit("File not found")
except OSError as e:
    sys.exit(f"Not a Python file")
