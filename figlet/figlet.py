# figlet.py
# Kelis Hightower

# importing the libraies and functions I plan on using
from pyfiglet import Figlet
import random
import sys


# settign "figlet" to the function that is Figlet
figlet = Figlet()

# a list of all the available font stored in figlet
fonts = figlet.getFonts()
# if the user inputs no additonal arguments other than .py then set the font to a ranom font using the the random comand
if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(fonts))
# if the user inputs 3 arguments with the correct syntax and specifc font, set the font to the third argument (2 index and where the font should have been inputed)
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    figlet.setFont(font=sys.argv[2])
# If neither is true state that there has been an invalid usage to the user
else:
    sys.exit("Invalid usage")

# Ask user for an input
text = input("Type: ")
# depening on the input print out the text in the font generated based on previous perameters
print(figlet.renderText(text))
