# shirtitficate.py
# Kelis Hightower

# I loved playing aorund with the deign elemnts

# imports the FPDF class from the fpdf module
from fpdf import FPDF


# gets name from user
name = input("Name: ")
# creates a new pdf object
pdf = FPDF()
# adds a new page to the pdf document
pdf.add_page()
# sets th efont to helvetica bold with a size 45 font
pdf.set_font("helvetica", "B", 45)
# adds a cell/ where the words with be oreinted on the shirt
pdf.cell(0, 60, "CS50 Shirtificate", align="C")
# adds the image I uploaded to the pdf
pdf.image("shirtificate.png", x=0, y=70)
# sets font size to 30
pdf.set_font_size(30)
# sets the text color
pdf.set_text_color(255, 255, 255)
# orents the text using cordinets and print out name took CS50
pdf.text(x=64, y=150, text=f"{name} took CS50")
# saves a new pdf as shirtificate.pdf = our output
pdf.output("shirtificate.pdf")
