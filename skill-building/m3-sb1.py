# m3-sb1.py
# Kelis Hightower

#cube = [1,3,5,7,9,11,13,15,17,19,21]
#for num in cube:
    #print(num, f"{num * num * num}")

#start = 1
#rate = float(input(" Give me an intrest rate"))
#years = 0
#while start < 2:
 #   start = start * (1+rate)
  #  years = years + 1
#print(years)

toys = {
    "race car": "Hallway closet",
    "Barbie": "Top shelf",
    "LEGOS": "Under the bed"
}

toy = input("Print out a toy")

try:
    print(f"You will find the {toy} in the {toys[toy]}")  # print out values from dict
# If not ignore it by printing out nothing
except KeyError:
    print("We don't have that toy")
