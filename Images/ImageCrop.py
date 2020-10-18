__author__ = 'Matheus Ruggeri' 
ImageFilesSource = 'https://www.searchpng.com/download-png/?imageid=11850'
ImageFilesSource = 'https://www.searchpng.com/download-png/?imageid=7219'


from PIL import Image

X_start = 0
Y_start = 470
X_Size = 2048
Y_Size = 1096 + Y_start

img = Image.open("PC.png")
img = img.crop( (X_start, Y_start, X_Size, Y_Size) )

file_destination='PC_Crop.png'

imagefile = open(file_destination, 'wb')
try:
    img.save(imagefile, "png", quality=100)
    imagefile.close()
except:
    print ("Error")
#Screen start -> 360,85
    
    
X_start = 510
Y_start = 41
X_Size = 1447 + Y_start
Y_Size = 2048 - Y_start

img = Image.open("Smartphone.png")
img = img.crop( (X_start, Y_start, X_Size, Y_Size) )

file_destination='Smartphone_Crop.png'

imagefile = open(file_destination, 'wb')
try:
    img.save(imagefile, "png", quality=100)
    imagefile.close()
except:
    print ("Error")
#Screen start -> 64,57