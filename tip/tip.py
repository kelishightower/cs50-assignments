# tip.py
# Kelis Hightower

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    dollars = dollars.strip("$")  # strip off the $ sign
    dollars = float(dollars)  # converts the value of percent into a float
    return dollars  # returns the new dollars value


def percent_to_float(percent):
    percent = percent.strip("%")  # strip off the % sign
    percent = float(percent)  # converts the value of percent into a float
    percent = percent/100  # divides the new float by 100 to convert into a decmible
    return percent  # returns the new percent value


main()
