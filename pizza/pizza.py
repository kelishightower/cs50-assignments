# # pizza.py
# # Kelis Hightower

# importing the needed files
# 1- to take command line arguments 2- to read csv files 3- impoting the styling format
import sys
import csv
from tabulate import tabulate


def main():
    # Check the number of command-line arguments (to see if theres only one input)
    if len(sys.argv) > 2:
        sys.exit("To many arguments")
    elif len(sys.argv) < 2:
        sys.exit("To few arguments")

    # assigns a varible to the inuted argument stored as file name
    filename = sys.argv[1]
    # checks to see if the file end with csv and if not send a exit error messasge
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    # Try to open and read the csv file
    try:
        with open(filename, "r") as csvfile:
            reader = csv.reader(csvfile)
            # reads the header from the file
            headers = next(reader)
            # reads the rest of the data from the file
            data = list(reader)
            # Print the table in te desired format
            print(tabulate(data, headers=headers, tablefmt="grid"))
    # exception errors that if caught will send a exit message
    except FileNotFoundError:
        sys.exit("File not found")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")


# calls main
if __name__ == "__main__":
    main()
