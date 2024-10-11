# bitcoin.py
# Kelis Hightower

# importing all libraies that will be used
import requests
import sys
import json

# checking to see if the user inputed an argument in the terminal (ammount of bitcoin to test) (python... number) if it dosent print out error message
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
# if everything checks out get information from the api linked
else:
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # try to convert the input to a float, if that dosent work (Value error) print out an error message that no number was entered
    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("Command line is not a number")
    # requesting the data from the linked api
    data = request.json()
    # bpi access the overall data in the link and extracts the overall bpi list
    bpi = data["bpi"]
    # used goes into the bpi list and extracts the USD listed
    usd = bpi["USD"]
    # price goes into the usd list and extract the listen rate  (a tower of accessing to reach the desired value)
    price = usd["rate"]
    # removes the commas from the output given by the api
    price = price.replace(",", "")
    # multiplies the price requested times the useres input converting both to floats
    price = float(price) * float(sys.argv[1])
    # last prining out the price in the desired format
    print(f"${price:,.4f}")
