__author__ = 'Matheus Ruggeri' 
ImageFilesSource = 'https://www.searchpng.com/download-png/?imageid=11850'
ImageFilesSource = 'https://www.searchpng.com/download-png/?imageid=7219'

'''
Procedure:
    Import the images.
    Check the size of the print screen and compare with the screen size in the template
    If the print is larger, expands the template by copy/past some lines in the figure


'''

from PIL import Image
import sys

file_destination='SP_Print_Save.png'
imagefile = open(file_destination, 'wb')

SP = Image.open('Images/Smartphone_Crop.png')
SP_width, SP_height = SP.size
# Screen Square -> (64,57) - (914,57) / (64,1900) - (914,1900)
Screen_X_Size = 914 - 64 + 1
Screen_Y_Size = 1900 - 57 + 1

Print_SP = Image.open('Print_SP.png')
Print_SP_width, Print_SP_height = Print_SP.size


# Crop the important parts of image
SP_Left = SP.crop( (0, 0, 489, SP_height) )
SP_Center_Line = SP.crop( (489, 0, 489+1, SP_height) )
SP_Right = SP.crop( (490, 0, 490+489, SP_height) )


xPosition = 0
yPosition = 0
addedLines = 0

if (Print_SP_width < Screen_X_Size):
    ratio = (Screen_X_Size/Print_SP_width)
    Print_SP = Print_SP.resize([int(Print_SP_width * ratio), int(Print_SP_height * ratio)], Image.ANTIALIAS) 
    Print_SP_width, Print_SP_height = Print_SP.size
    
    
if (Print_SP_width >= Screen_X_Size):
    New_Image_X = SP.size[0] + Print_SP_width - Screen_X_Size
    New_Image_Y = SP.size[1]
    SP_New_Image = Image.new('RGBA', (New_Image_X, New_Image_Y))
    
    SP_New_Image.paste(SP_Left, (xPosition, yPosition))
    
    Num_new_columns = Print_SP_width - Screen_X_Size
    xPosition = xPosition + SP_Left.size[0]
    
    while (addedLines <= Num_new_columns/2):
        addedLines += 1
        SP_New_Image.paste(SP_Center_Line, (xPosition,yPosition))
        xPosition = xPosition + SP_Center_Line.size[0]
    
    SP_New_Image.paste(SP_Right, (xPosition,yPosition))
    xPosition = xPosition + SP_Right.size[0]
else:
    print("Image too small X")
    sys.exit()
    
SP_New_Image.save(open("Temp/XsizeFixed.png", 'wb'), "png", quality=100)
SP_New_Image.close()

SP_Temp_Image = Image.open("Temp/XsizeFixed.png")
SP_Temp_width, SP_Temp_height = SP_Temp_Image.size

# Crop the important parts of image
SP_Top = SP_Temp_Image.crop( (0, 0, SP_Temp_width, 983) )
SP_CenterLine = SP_Temp_Image.crop( (0, 983, SP_Temp_width, 983+1) )
SP_Bottom = SP_Temp_Image.crop( (0, 983, SP_Temp_width, 983+983) )

xPosition = 0
yPosition = 0
addedLines = 0

if (Print_SP_height > Screen_Y_Size or True):
    New_Image_X = SP_New_Image.size[0]
    New_Image_Y = SP_New_Image.size[1] + Print_SP_height - Screen_Y_Size
    SP_New_Image = Image.new('RGBA', (New_Image_X, New_Image_Y))
    
    Num_new_lines = Print_SP_height - Screen_Y_Size
    
    SP_New_Image.paste(SP_Top, (xPosition, yPosition))
    yPosition = yPosition + SP_Top.size[1]
    
    while (addedLines < Num_new_lines):
        addedLines += 1
        SP_New_Image.paste(SP_CenterLine, (xPosition, yPosition))
        yPosition = yPosition + SP_CenterLine.size[1]
    
    SP_New_Image.paste(SP_Bottom, (xPosition, yPosition))
    yPosition = yPosition + SP_Bottom.size[1]
        
else:
    print("Image too small Y")
    sys.exit()
    
SP_New_Image.save(open("Temp/Ready.png", 'wb'), "png", quality=100)


layer1 = Image.new('RGBA', (New_Image_X, New_Image_Y))
layer2 = Image.new('RGBA', (New_Image_X, New_Image_Y))

layer1.paste(Print_SP, (64,57))
layer2.paste(SP_New_Image, (0,0))

Image.alpha_composite(layer1, layer2).save("Combined_SP.png")

SP_New_Image.close()