# grocery.py
# Kelis Hightower

def main():
    # creating an empty dictionary
    list = {}

    while True:
        try:
            # Gets the users inptut
            item = input().upper()
            # checks to see if item in is ALREADY the list, if so make the value 1 additonal ammount
            if item in list:
                list[item] = list[item] + 1
            # if its not in the list yet set the value to 1
            else:
                list[item] = 1
        # if controll d is clicked exacute the following
        except EOFError:
            # print a new line
            print()
            # break out of the loop
            break
    # fills our empty list above with the inputed values
    items = set(list)
    # sort the list
    items = sorted(items)
    # now tht we have a filled dict, iterate though it and print out how many and the inputed value
    for item in items:
        print(f"{list[item]} {item}")


# laslty call the main function
main()
