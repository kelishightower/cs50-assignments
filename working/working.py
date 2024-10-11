# working.py
# Kelis Hightower
import re

# calls the convert function below and takes the input as the argument (or the thing to convert)


def main():
    print(convert(input("Hours: ")))

# take the users input and checks if its the proper format
# Group 1 - First time hour
# Group 2 - First times minutes
# Group 3 - First times AM/PM
# Group 4 - Second times hour
# Group 5 - Second times minutes
# Group 6 - Second times AM/PM


def convert(s):
    timeGroups = re.search(
        r"^([1-9]|[1][0-2])(?:\:([0-5][\d]))?\s([aApP][mM])\sto\s([1-9]|[1][0-2])(?:\:([0-5]\d))?\s([aApP][mM])$", s, re.IGNORECASE)
    #
    if timeGroups != None:
        # For the first of the two times checks to see if it is 12AM or midnight (looking at the hours for the next few lines only)
        if timeGroups.group(1) == "12" and timeGroups.group(3).lower() == "am":
            # if it is, convert it into 24 hour format (00)
            firstTime = "00"
        # Checks if the first time is less than 12 and in the PM
        # If so converts it into 24 hour format...
        elif int(timeGroups.group(1)) < 12 and timeGroups.group(3).lower() == "pm":
            # Adds the number from the first time to 12 to get the deisred 24 hour number (1+12 = 13:00)
            firstTime = str(int(timeGroups.group(1)) + 12).zfill(2)
        # Converts in into 24 hour format and simply checks/ensures it has the right amount of trailing digits
        # keeps as is (could already be in the right format) or makes sure it has 2 digits
        else:
            firstTime = timeGroups.group(1).zfill(2)

        # For the first time but now looking at the minutes group (if the input has minutes)
        if timeGroups.group(2) != None:
            # adds the minutes form the input to the hour making sure there 2 digits
            firstTime = firstTime + f":{timeGroups.group(2).zfill(2)}"
        # If there are no minutes just input a default of 00
        else:
            firstTime = f"{firstTime}:00"

        # Moving to the second of the two inputed time, checks to see if its midnight AND there are no minutes inputed or is compleimted with the default of 00
        if (timeGroups.group(4) == "12" and timeGroups.group(6).lower() == "am" and (timeGroups.group(5) == None or timeGroups.group(5) == "00")):
            # converts the time to 24 format
            secondTime = "00"
        # Checks if the secondtime is less than 12 and in the PM
        elif int(timeGroups.group(4)) < 12 and timeGroups.group(6).lower() == "pm":
            # Converts to 24 hour format with two digits
            secondTime = str(int(timeGroups.group(4)) + 12).zfill(2)
        # If none of the above either keep as is or re-configure so it has two digtis
        else:
            secondTime = timeGroups.group(4).zfill(2)

        # FOr the minutes portion of the second inputed time checks to see if any minutes were stated
        if timeGroups.group(5) != None:
            # if yes, add it to the hour and confure the mintures so its in 24 hour format(2 digits)
            secondTime += f":{timeGroups.group(5).zfill(2)}"
        # if no mintues just keep as the default
        else:
            secondTime = f"{secondTime}:00"
        # returns the finished prodcuts with all the reconfigurations
        return f"{firstTime} to {secondTime}"
    # Error arieses if the regular expression didnt match the groups in anyway (invalid format)
    else:
        raise ValueError


# call the main function
if __name__ == "__main__":
    main()
