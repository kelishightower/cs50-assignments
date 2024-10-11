# plates.py
# Kelis Hightower

# Define a main function
def main():
    # Get input from the user
    plate = input("Plate: ")
    # Call the is_valid() function with the plate entered
    if is_valid(plate):
        # plate is valid since is_valid() returned True
        print("Valid")
    else:
        # plate is not valid since is_valid() returned False
        print("Invalid")

# definting a funtion called is Valif that checked if the imput is...valid


def is_valid(s):

    # First checking to see if the entered plate in more that two chracters and less than 6 characters if not it will return false
    if len(s) < 2 or len(s) > 6:
        return False
# Checks to see if both the first adn second letter in the string are both letters from a-z if not then the program will return false
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
# This for loop iterates thorugh each letter in the string to isure that each charcter is indeed a number or a letter is not it will return false
    for character in s:
        if character.isalnum() == False:
            return False
# This acts as a logic checker, something to refer to when decided is a condition is valid or not
    firstNumber = True
# Iterating through the scnetence using the len() fuc that allows it to go thorugh the entire length of the string
    for i in range(len(s)):
        # checks if there is a number in the plate entered (at this point the plate could still be valid)
        if s[i].isdigit():
            # Enteres another for loop that uses the i: feature to check to see if there is a letter vlaue on the end which is not allowed if there is a number before it
            if not s[i:].isdigit():
                return False
# If there is a number and the number is of a value of 0 it will return false
            if s[i] == "0" and firstNumber == True:
                return False
# if both of these conditions are not mtet (and) then it will also return false
            else:
                firstNumber = False
    # We made it through all of the checks above so we must now have a valid Vanity Plate
    return True


# Call the main() function to start the program
if __name__ == "__main__":
    main()
