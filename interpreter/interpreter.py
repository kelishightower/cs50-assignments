# interpreter.py
# Kelis Hightower

# gets expression from user
expression = input("Enther expression:  ")
# splits the expression (by cutting at the spaces) then assinging num1 to x numb2 to x and the opperator to y
x, y, z = expression.split(" ")
# set of if statments that say how to evaluate x and z based off what the user typed in second (or y)
if y == "+":
    print(f"{float(x) + float(z)}")
elif y == "-":
    print(f"{float(x) - float(z)}")
elif y == "/":
    print(f"{float(x) / float(z)}")
elif y == "*":
    print(f"{float(x) * float(z)}")
elif y == "%":
    print(f"{float(x) % float(z)}")
