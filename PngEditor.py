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

file_destination='PC_Print_Save.png'
imagefile = open(file_destination, 'wb')

PC = Image.open('Images/PC_Crop.png')
PC_width, PC_height = PC.size
# Screen Square -> (360,85) - (1686,85) / (360,926) - (1686,926)
Screen_X_Size = 1686 - 360
Screen_Y_Size = 926 - 85

Print_PC = Image.open('Print_PC.png')
Print_PC_width, Print_PC_height = Print_PC.size


# Crop the important parts of image
PC_Left = PC.crop( (0, 0, 360, PC_height) )
PC_Left_Line = PC.crop( (361, 0, 361+1, PC_height) )
PC_Left2Center = PC.crop( (361, 0, 870, PC_height) )
PC_Center = PC.crop( (870, 0, 870+315, PC_height) )
PC_Center2Right = PC.crop( (1185, 0, 1185+501, PC_height) )
PC_Right_Line = PC.crop( (1532, 0, 1532+1, PC_height) )
PC_Right = PC.crop( (1686, 0, 1686+360, PC_height) )


xPosition = 0
yPosition = 0
addedLines = 0

if (Print_PC_width > Screen_X_Size):
    New_Image_X = PC.size[0] + Print_PC_width - Screen_X_Size
    New_Image_Y = PC.size[1]
    PC_New_Image = Image.new('RGBA', (New_Image_X, New_Image_Y))
    
    PC_New_Image.paste(PC_Left, (xPosition, yPosition))
    
    Num_new_columns = Print_PC_width - Screen_X_Size
    xPosition = xPosition + PC_Left.size[0]
    
    while (addedLines <= Num_new_columns/2):
        addedLines += 1
        PC_New_Image.paste(PC_Left_Line, (xPosition,yPosition))
        xPosition = xPosition + PC_Left_Line.size[0]
    
    PC_New_Image.paste(PC_Left2Center, (xPosition,yPosition))
    xPosition = xPosition + PC_Left2Center.size[0]
    
    PC_New_Image.paste(PC_Center, (xPosition,yPosition))
    xPosition = xPosition + PC_Center.size[0]
    
    PC_New_Image.paste(PC_Center2Right, (xPosition,yPosition))
    xPosition = xPosition + PC_Center2Right.size[0]
    
    while (addedLines <= Num_new_columns):
        addedLines += 1
        PC_New_Image.paste(PC_Right_Line, (xPosition,yPosition))
        xPosition = xPosition + PC_Right_Line.size[0]
    
    PC_New_Image.paste(PC_Right, (xPosition,yPosition))
    xPosition = xPosition + PC_Right.size[0]
    
PC_New_Image.save(open("Temp/XsizeFixed.png", 'wb'), "png", quality=100)
PC_New_Image.close()

PC_Temp_Image = Image.open("Temp/XsizeFixed.png")
PC_Temp_width, PC_Temp_height = PC_Temp_Image.size

# Crop the important parts of image
PC_Top = PC_Temp_Image.crop( (0, 0, PC_Temp_width, 548) )
PC_CenterLine = PC_Temp_Image.crop( (0, 548, PC_Temp_width, 548+1) )
PC_Bottom = PC_Temp_Image.crop( (0, 548, PC_Temp_width, 548+548) )

xPosition = 0
yPosition = 0
addedLines = 0

if (Print_PC_height > Screen_Y_Size):
    New_Image_X = PC_New_Image.size[0]
    New_Image_Y = PC_New_Image.size[1] + Print_PC_height - Screen_Y_Size
    PC_New_Image = Image.new('RGBA', (New_Image_X, New_Image_Y))
    
    
    Num_new_lines = Print_PC_height - Screen_Y_Size
    
    PC_New_Image.paste(PC_Top, (xPosition, yPosition))
    yPosition = yPosition + PC_Top.size[1]
    
    while (addedLines <= Num_new_lines):
        addedLines += 1
        PC_New_Image.paste(PC_CenterLine, (xPosition, yPosition))
        yPosition = yPosition + PC_CenterLine.size[1]
    
    PC_New_Image.paste(PC_Bottom, (xPosition, yPosition))
    yPosition = yPosition + PC_Bottom.size[1]
    
PC_New_Image.save(open("Temp/Ready.png", 'wb'), "png", quality=100)
PC_New_Image.close()


PC.paste(Print_PC, (360, 85))
PC.save('mix.png')
PC.close()