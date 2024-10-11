# response.py
# Kelis Hightower


# imports the chckers funcion from the vlaidators collection
from validator_collection import checkers


def main():
    print(validate(input("What's your email adress? ")))


def validate(email):
    # Check to see if the inputed email is valid using a library function checkers.is_email()
    # like a built in email pattern already stored in the library that we can quickly corss check
    if checkers.is_email(email):
        # if it matches great... return Valid
        return "Valid"
    # doesent match... awww retun Invalid
    else:
        return "Invalid"


# calls maincd
if __name__ == "__main__":
    main()
