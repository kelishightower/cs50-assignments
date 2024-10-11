# shirt.py
# Kelis Hightower

# allows the user to input command line arguments that can be used by the follwoing code
import sys
# imports Image which allows the coder to work with and manipulate images,
# and ImageOps that contains image processing opperationsfrom the Python Imaging Library
from PIL import Image, ImageOps
# "ooperating-system dependant functuality" which allows you to interact with files realted to the "OS"
import os


def main():
    # if the commanf line is less than 3 in length say to few and exit
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # if its more say to many and exit
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # If it equals 3 (what we want) split the last and seocond to last thing inputed and make it file1 and file2
    if len(sys.argv) == 3:
        # os.path allows yout owork with files and directory paths
        # path.splitext allows you to split the directory path so that it contian multiple elemnets ("the root and the extension")
        # in short breaks it (the file/directory) up to assign argv 1 to file1 and argv 2 to file2
        file1 = os.path.splitext(sys.argv[1])
        file2 = os.path.splitext(sys.argv[2])

        # file1[1] access the file part of the tuple that it was broken up into in the previous lines
        # makes the input case insensitive
        # then sees if the file extnetions were looking are vlaid file inputs
        # if not the same say its invalid and exit
        if file1[1].lower() != ".jpg" and file1[1].lower() != ".png":
            print("Invalid input")
            sys.exit("Invalid input")
        # vise versa, and if so also exit and say its invalid but with file 2
        if file2[1].lower() != ".jpg" and file2[1].lower() != ".png":
            sys.exit("Invalid input")
        # this then checks to see if they are the same type fo file (png, jpeg, ect)
        if file1[1].lower() != file2[1].lower():
            sys.exit("Files must have the same extension")
    # opens the image using the Image opperation we imported eariler and assigned into the varible shirt
    shirt = Image.open("shirt.png")
    try:
        # opend the file that is our first arguments (after python file.py) and assignes as the befroe picture
        before = Image.open(sys.argv[1])
    # if the file is not downloaded/unzippsed/cannot be found exit and say the file doesnt exsist
    except IOError:
        sys.exit("Input file does not exist")
    # this part of the code is manipulating the image using the ImageOps function we imported earlier

    before = ImageOps.fit(
        # 1- fits it to be 600x600 pixels 2- BICUBIC = high quality (in simple terms) 3- bleed = acts as a baorder 4- centering = well keeps it centered
        before, (600, 600), method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5)
    )
    # take the beofre image and overlay the shirt image. (what to overalay, the mask) in this case the shirt is both the argumetns
    before.paste(shirt, shirt)
    # saves the image we just made in the line above and save it to the file we specified by out seocnd argument in our command line
    before.save(sys.argv[2])
    # everything went according to plan so now its time to exit the program :)
    sys.exit(0)


# calls the main function
if __name__ == "__main__":
    main()
