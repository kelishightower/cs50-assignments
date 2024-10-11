# seasons.py
# Kelis Hightower

# imports date class from datetime module
from datetime import date
# imports inflect modle (words---> numbers )
import inflect
# import sys to uses things like sys.exit
import sys

# creates an inflect engine object used to convert words into numbers
p = inflect.engine()


def main():
    try:
        # gets date from user and attemps to split it by the - into 3 different varibles
        year, month, day = input("Enter date: ").split("-")
    # if it dosent a vlaue error should occur is so..
    except TypeError and ValueError:
        # exit the program and print out the message
        sys.exit("Invalid date")
    # prints the results from calling total_minutes funtion on our inputs
    print(total_minutes(year, month, day))

# creates a func that takes 3 parameters


def total_minutes(year, month, day):
    # try to create an object from our inputs
    try:
        dt = date(int(year), int(month), int(day))
    # if it dosent work, handle the erorr by returning "Invalid date" to where the func was called
    except ValueError:
        return "Invalid date"
    # gets todays date with a imported today() func
    tday = date.today()
    # calucaltes the ammount of time passed by subtracting today - the objected we created from out inputed date
    diff = tday - dt
    # converts the above differece into minutes
    minutes = int(diff.total_seconds() / 60)
    # converts the number of mins into words using the imported numbers_to_words func
    msg = p.number_to_words(minutes, andword="") + " minutes"
    # returns the new message but capitalizes the first letter
    return msg.capitalize()


# calls the main functon
if __name__ == "__main__":
    main()
