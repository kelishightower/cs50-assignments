# nutrition.py
# Kelis Hightower


# Created a dict names fruit that contains the list from the poster pdf
fruit = {
    "apple": {"calories": 130},
    "avocado": {"calories": 50},
    "banana": {"calories": 110},
    "cantaloupe": {"calories": 50},
    "grapefruit": {"calories": 60},
    "grapes": {"calories": 90},
    "honeydew melon": {"calories": 50},
    "kiwifruit": {"calories": 90},
    "lemon": {"calories": 15},
    "lime": {"calories": 20},
    "nectarine": {"calories": 60},
    "orange": {"calories": 80},
    "peach": {"calories": 60},
    "pear": {"calories": 100},
    "pineapple": {"calories": 50},
    "plums": {"calories": 70},
    "strawberries": {"calories": 50},
    "sweet cherries": {"calories": 100},
    "tangerine": {"calories": 50},
    "watermelon": {"calories": 80},

}

# asking user to input a fruit from above
type = input("Enter the zip code you want the weather for: ").lower()
# checking to see if the input is apart of the preset dict of fruits if so print out the calories...
# side note, I know we did not learn this specific thing in class but I was able to search up a conditional that works (I hope that's ok)
if type in fruit:
    print(fruit[type]["calories"])  # print out values from dict
# If not ignore it by printing out nothing
else:
    print("")
