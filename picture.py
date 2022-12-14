from PIL import Image,ImageFilter,ImageFont,ImageDraw
im = Image.open("cloud.jpg")
out = im.filter(ImageFilter.CONTOUR())
ttfont = ImageFont.truetype("C:\\Windows\\Fonts\\Arial\\arial.ttf",100)
draw = ImageDraw.Draw(out)
draw.text((150,500), "The Earth",font = ttfont , fill=(0,0,0,255))
out.show()
out.save("edited-earth.jpg")