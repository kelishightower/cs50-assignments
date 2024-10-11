# coke.py
# Kelis Hightower

# Initialize conatiner variables due = the set price of a coke can
# amount is the variable we update to track how main "coins" the user has entered"
due = 50
amount = 0
# While look that runs everytime the ammount is less than 50 (or you have yet to pay the full amount)
while amount < 50:
    # Start off my reminding the user of how much they owe/ still owe which is updated after every input
    print("Amount Due:", due - amount)
    # Varible coin is created to store the amount the user inputs
    coin = int(input("Insert Coin: "))
    # this insures that the coin value fits into out parmteres of equaling 10, 5 or 25
    if coin == 25 or coin == 10 or coin == 5:
        # If the amount is valid we can then add it to our amount paid
        amount = coin + amount
    # If we are in the situation where the ammount paid is above 50 cents it spits out the change (or how much over 50 it is)
    if amount >= 50:
        # printing out the change
        print("Change Owed:", amount - 50)
