from PIL import Image

images = [Image.open(x) for x in ['Temp/Combined_PC.png', 'Temp/Combined_SP.png']]

New_Image_X = images[0].size[0]
New_Image_Y = images[0].size[1]

layer1 = Image.new('RGBA', (New_Image_X, New_Image_Y))
layer2 = Image.new('RGBA', (New_Image_X, New_Image_Y))

width_SP, height_SP = images[1].size
Smartphone_Resize = images[1].resize([int(width_SP/1.7), int(height_SP/1.7)], Image.ANTIALIAS) 

layer1.paste(images[0], (0,0))
layer2.paste(Smartphone_Resize, (2000,160))

Image.alpha_composite(layer1, layer2).save("Combined_Both.png")
