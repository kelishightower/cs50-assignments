# adieu.py
# Kelis Hightower

# Establishes the inflect library and its functions
import inflect

inflectEngine = inflect.engine()

# creates an empty string to store the "persons" inputed by the user
people = []

while True:
    # Asks user for a name and adds said name to the list one by one
    try:
        person = input("Enter a name: ")
        people.append(person)
    # if the user hit controll d exit the lop
    except EOFError:
        break
# print a blank line
print()
# First print the common starter phrace followed by the list of people in the ajoined fashion
print(f"Adieu, adieu, to", inflectEngine.join(people))
