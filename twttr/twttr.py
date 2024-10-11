# twttr.py
# Kelis Hightower

# Asks the user for a input
def main():
    # gets word from user
    word = input("Enter a name: ")

# makes new varible based off of the restults from the shorten function
    noVowel = shorten(word)
# prints out the newly shortened word
    print("Output: " + noVowel)


def shorten(word):
    # creating a container varible that stores the string I plan to rebuild later on in the program
    temp = ""
# Creating a for loop at itterates through the string and checks to see if its eqaul to a vowel (upper or lower)
    for letter in word:
        if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            temp += letter
        # laslty returns the new string we created
    return (temp)


# calls main
if __name__ == "__main__":
    main()
