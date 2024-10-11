# meal.py
# Kelis Hightower

# Conversion function that..
def convert(theTime):
    # 1) splits the input and stores them in hour and minute variables...
    hour, minute = theTime.split(":")
    # Changes the hour input for hour into a string (so we can manipulate them better later)
    hour = int(hour)
    # Same as above
    minute = int(minute)
    # Now we are reassigning what the overall "theTime" varible is by adding both integeres into one number that we cna then compare later
    # and dividing minutes by 60 so we know how much of the hour has passed in a decimal form
    theTime = hour + minute/60
    # finally we return are newly manipulated "theTime" var back to where it is being called
    return theTime


def main():
    # Takes input from user...
    theTime = input("Enter a time: ")
    # Calls the convert funtion to re-assign theTime using our convert function inorder to continue on with the int if statments below
    theTime = convert(theTime)

    # Seires of if statment that put the "theTime" value into a range and compare it to see if it fall into one of the the meal options
    if theTime >= 7 and theTime <= 8:
        print("breakfast time")
    elif theTime >= 12 and theTime <= 13:
        print("lunch time")
    elif theTime >= 18 and theTime <= 19:
        print("dinner time")


# Laslty I call main which preforms both of the functions created
if __name__ == "__main__":
    main()
