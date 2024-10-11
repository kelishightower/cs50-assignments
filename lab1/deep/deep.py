# deep.py
# Kelis Hightower


# Taking a response from user along with removing and white spaces and
# converting the input to lower case making it case insensitive
response = input("What is the meaning of life? ").strip().lower()

# Comparing the inputed string to what I qualfied as "right answers" if not then print out no
match response:
    case "42":
        print("Yes")
    case "forty-two":
        print("Yes")
    case "forty two":
        print("Yes")
    case _:
        print("No")
