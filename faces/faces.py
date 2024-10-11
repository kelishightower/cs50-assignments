# face.py
# Kelis Hightower

# main function that call the convert function white assigning a value to the phrase variable
def main():
    phrase = input("What's your name? ")
    # calling convert function
    convert(phrase)

# creating the convert function with a phrase parameter/argument


def convert(phrase):
    print(phrase.replace(':)', '🙂').replace(":(", "🙁"))


main()
