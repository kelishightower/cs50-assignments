# um.py
# Kelis Hightower

# imports so you can use regular expression
import re


def main():
    # print the results from the function count being called on the input from the user
    print(count(input("Type here: ")))


def count(s):
    # goes through the string to fine all the occurances of "um" (case insensitive)
    word_count = re.findall(r"\b(um)\b", s, re.IGNORECASE)
    # returns the number of occurnces it found
    return len(word_count)


# calls main
if __name__ == "__main__":
    main()
