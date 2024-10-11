# game.py
# Kelis Hightower

import random

# set the target number to a random integer before playing the game
goal = random.randint(1, 100)

# Set a main funtion


def main():
    # A loop to test weather the inputed level is valid
    while True:
        try:
            level = int(input("Level: "))
            # if the input is a postitive int (its valid), breaks out of the loop
            if level >= 0:
                break
            # if its not valid reprompt the user
            else:
                continue
        # if its not a int at all, reprompt the user again
        except ValueError:
            continue

    while True:
        # Sees if the Guess input is an int if not re prompt the user
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue
        # if your guess matches the goal print "Just right" and break out of the loop (because you won)
        if guess == goal:
            print("Just right!")
            break
        # If its to big print too large and reprompt
        elif guess > goal:
            print("Too large!")
        # if its too small print too small and reprompt
        elif guess < goal:
            print("Too small!")
        # if all else goes wrong reprompt user
        else:
            continue


# calls the main function
if __name__ == "__main__":
    main()
