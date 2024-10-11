# camel.py
# Kelis Hightower


# takes input from user
name = input("Enter a word:")

# Check if name is an empty string
if name == "":
    print("name must not be empty")
    # Exit the program and exit 1 (My dad is a software engineer, he added that in as a small teaching moment but I do note we have not learned it in this course)
    exit(1)

# check is first char is capital and replace it with lower case as camel case can begin with a capital
if name[0].isupper():
    name = name.replace(name[0], name[0].lower(), 1)
# Establish a while loop that runs when the string is NOT all lowercase
while not name.islower():
    # embeded is a for loop that check each char in the string
    for i in range(0, len(name)):
        # Checks if the char is upper
        if name[i].isupper():
            # if so replace it with the lowercase version along with a "_"
            name = name.replace(name[i], "_" + name[i].lower(), 1)
# Laslty print name
print(name)
