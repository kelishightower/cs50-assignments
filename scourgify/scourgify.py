# scourgify.py
# Kelis Hightower

# uses and works with csv files
import csv
# use and work with the command line
import sys

# checks the number of command-line arguments
# more than 3 exit and say to many and vise versa if less than 3
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# checks to see if the file has a csv extension if not say this isnt a csv file and exit the program
if not sys.argv[1].endswith("csv"):
    sys.exit("Not a csv file")

# assign the first argument with the var input_file and the second with the var output_file
input_file = sys.argv[1]
output_file = sys.argv[2]

#
try:
    # opens the first argument file as a file we can only read
    with open(sys.argv[1]) as file:
        # treats the csv file like a dictionary so it can read it row by row later on
        reader = csv.DictReader(file)
        # opens the seondly called file as a file we can write in
        with open(sys.argv[2], 'w') as file2:
         # says the file 2 should have their headers names first, last, and house (or feildnames)
            writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
            # writes the new deaher using the field names with the writeheader funtion
            writer.writeheader()
            # goes through each row in the reading file (first argument )
            for row in reader:
                # removes the orginal header of name in the row and replaces it with first
                row["first"] = row.pop("name")
                # splits the new values under first
                last_name, first_name = row["first"].split(", ")
                # after spliting it breaks it up into first and last name
                row["first"] = first_name
                row["last"] = last_name
                # with all the new chnages it i snow rewriteen into our write file
                writer.writerow(row)
# checks to se if the file is there if not say file was not found
except FileNotFoundError:
    sys.exit("File not found")
