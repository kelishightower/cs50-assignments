# taqueria.py
# Kelis Hightower

# Defining a main function
def main():

    # Creates a dict that assigns an item with a price
    items = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    # Set a container variable names total
    total = 0
    while True:
        try:
            # asking user for an input and convertitng it to title format
            item = input("Item: ").title()
            # if the input is in the dictionary then contniue on with the code
            if item in items:
                # Accumilates the total based off the price assotiate with the item and keeps a running total
                total = total + items[item]
            # print of the total based on the fiven format (dollar amount)
            print(f"Total: ${total:.2f}")
        # If there the user does controll d then break out of the loop
        except EOFError:
            break


# lastly call the main function
main()
