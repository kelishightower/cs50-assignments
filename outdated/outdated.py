# outdated.py
# Kelis Hightower
# creating a main function
def main():
    # creating a list to store the months
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        # Prompting the user for input (asking for the date)
        date = input("Date: ").title()
        # sees if the date contains a / (if the values are seperated by a /)
        if "/" in date:
            try:
                # split the string into 3 parts (month,day,year) by the / charcter
                month, day, year = date.split("/")
                # converting all the values to ints
                month = int(month)
                day = int(day)
                year = int(year)

                # checks to see if its a valid month (between 1 and 12 inclusive) and if the day it valid 1 to 31 inclusive

                if (1 <= month <= 12) and (1 <= day <= 31):
                    # if everything checks out print the year followed by a - the month - and the day in the YYYY-MM-DD format
                    print(f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}")
                    # Everything checks out in the print so break out the loop
                    break
                # if everything does not check out then reprompt the user until they enter a valid date
                else:
                    continue
            # if a ValueError (like a string value) comes up repromt the user
            except ValueError:
                continue
        # if the string does NOT contain a / but a , continue on with the code
        elif "," in date:
            try:
                # Once again split the string
                month, day, year = date.split(" ")
                # if input string contains a month in the list month, assign the value month to the coresponding index + 1 (as python starts at 0)
                if month in months:
                    month = months.index(month) + 1
                # if not reprompt the user untill there a valid month from the list
                else:
                    continue
                # since the day is followed by a comma strip it off and convert it into a int
                day = day.strip(",")
                day = int(day)

                # Checks to see if its a valid day
                if 1 <= day <= 31:
                    # once again print out the date in thedesired format as stated above
                    print(f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}")
                    # once that is done break out of the loop
                    break
                # if not a valid day reprompt the user
                else:
                    continue
            # if it comes upon a ValueError repromt the user
            except ValueError:
                continue


main()
