#Creating Coordinates 
   
    

# Content
fileName =input("Save Document As, Enter with(.pdf) :-")
documentTitle =input("Enter Title for Document :-")
title = input("Enter Header :-")
subTitle = input("Enter SubTitle :-")
textLines =[
"Hey ,Guys My name is Tanay Padar. I am 16 year",
"old.I started this channel to share my Coding ",
"Knowledge and I will upload cool Python Project on",
"channel.Hope You will Support Me.",
"Language ---> Python",
"Instagram ---> tanay_30104",
"Snapchat ---> tanay_301004",
"Github ---> JuniorProgrammer30104"
]
image  =input("Enter Location of Image with (.pnj/.jpg) :-")

# Create document 
from reportlab.pdfgen import canvas 
pdf = canvas.Canvas(fileName)
pdf.setTitle(documentTitle)



# Create Header
pdf.setFillColorRGB(0, 0,225)
pdf.setFont("Courier-Bold",34)
pdf.drawCentredString(300,770, title)

# Create Sub Title 
# RGB - Red Green and Blue
pdf.setFillColorRGB(225, 0, 0)
pdf.setFont("Courier-Bold",26)
pdf.drawCentredString(290,720, subTitle)

# Draw a line
pdf.line(30, 710, 560, 710)

# Main Paragraph
from reportlab.lib import colors
text = pdf.beginText(30, 550)
text.setFont("Courier", 20)
text.setFillColor(colors.black)
for line in textLines:
    text.textLine(line)
pdf.drawText(text)

# Draw a image
pdf.drawInlineImage(image, 210, 562)
pdf.save()