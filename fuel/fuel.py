# fuel.py
# Kelis Hightower


# Define the main function
def main():
    fraction = input("Enter a Fraction")
    new_fraction = convert(fraction)
    output = gauge(new_fraction)
    print(output)


def convert(fraction):
    while True:

        try:  # trying the following code
            # Spliting the strong into left and right of the fraction
            numerator, denominator = fraction.split("/")
            numerator = int(numerator)  # seeing if they are able to be converted into ints
            denominator = int(denominator)
            # varible to hold the new value of fraction (frac)
            frac = numerator / denominator
            # retuns the value of p back to where the function was called
            if frac <= 1:
                p = int(frac * 100)
                return p
            # new way to say continue (I learned from my dad) else, prompt the messagea and pass (very similar to continue)
            else:
                fraction = input("Enter a Fraction: ")
                pass

        except (ValueError, ZeroDivisionError):  # if there a Value error raise the exception
            raise
# funtion for percent
def gauge(percentage):

    if percentage >= 99:  # checks to see if it clafies as full if so prints F
        return "F"
    elif percentage <= 1:  # checks to see if it could be clasified as empty if so print E
        return "E"
    else:  # if not full or empty simply return out the value in percent
        return(f"{percentage}%")

# calls main
if __name__ == "__main__":
    main()
