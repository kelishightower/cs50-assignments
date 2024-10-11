# watch.py
# Kelis Hightower

# imports so you can use regular expression
import re
# import sys to use sys exits
import sys


def main():
    # print the results from the function parse being called on the input from the user
    print(parse(input("HTML: ")))


def parse(s):
    # establishes pattern that takes multiple types of starters like https or www followed my the youtbe.com...
    result = re.search(r'.+src="https?://(?:www.)?youtube.com/embed/(.+?)"', s)
    # if the input from the user matched the pattern
    if result:
        # sets the varible line with the cancatination of https://youtu.be/ and the first group from the search function
        link = "https://youtu.be/" + result.group(1)
        # if theres a match return the link
        return link
    # if not return none
    else:
        return None


# calls the main function
if __name__ == "__main__":
    main()
