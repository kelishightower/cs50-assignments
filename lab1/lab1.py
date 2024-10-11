# lab1.py
# Kelis Hightower

# Constants
# All caps is how you declare vars with values that never change
LOCALTAXRATE = .10  # that's 10%
MEDICALRATE = .12  # That's 12%

# Storing user inputs in various variable containers + what type they should return (float,string, etc)
name = input("Enter name: ")
hourlyWage = float(input("Enter hourly wage: "))
hoursWorked = float(input("How many hours did you work this week?"))

# Perform calculations
if hoursWorked > 40:
    wages = 40 * hourlyWage
    overtimeWages = (hoursWorked - 40) * (hourlyWage * 1.5)
else:
    wages = hoursWorked * hourlyWage
    overtimeWages = 0

totalWages = wages + overtimeWages
taxes = totalWages * LOCALTAXRATE
medical = totalWages * MEDICALRATE
netPay = totalWages - taxes - medical

# Printing out a paystub
print()
print(f"Name: {name}")
print(f"Hourly wage: ${hourlyWage:.2f}")
print(f"Local taxes: ${taxes:.2f}")
print(f"Medical insurance: ${medical:.2f}")
print(f"Overtime pay: ${overtimeWages:.2f}")
print(f"Total gross earnings: ${totalWages:.2f}")
print(f"Net pay: ${netPay:.2f}")
