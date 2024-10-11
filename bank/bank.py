# bank.py
# Kelis Hightower

def main():
    # gets greeting from user
    greeting = input("Enter a greeting: ")
    # evaltues greeting based on the value funtion
    value(greeting)


def value(greeting):

    # Makes greeting case insensistive
    greeting = greeting.strip().lower()
# if statments to check the greeting and if contains the key word hello
    if greeting == "hello" or greeting.startswith("hello"):
        return 0
# Elif instead of if so it dosent print both 0 and 20 dollars
    elif greeting.startswith("h"):
        return 20
    # else returns 100 dollars
    else:
        return 100


# calls main
if __name__ == "__main__":
    main()
