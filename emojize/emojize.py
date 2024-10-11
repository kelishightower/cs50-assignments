# emojize.py
# Kelis Hightower

# import the emoji files
import emoji

# Ask user to input an emoji
user_input = input("Enter an emoji")

# Converts the input from the user into the emoji they requested into a new variable called output
output = emoji.emojize(user_input, language="alias")

# print out the converted text
print(output)
