from PIL import Image
import math

data = open("binaryfile.raw","rb").read()
width = 855
height = 8
pages = math.ceil(height/8)
assert len(data) == width * pages

img = Image.new("1", (width, height))
idx = 0
for page in range(pages):
    for x in range(width):
        b = data[idx]; idx += 1
        for bit in range(8):          # LSB = top pixel in page
            y = page*8 + bit
            if y < height:
                img.putpixel((x,y), (b >> bit) & 1)

img = img.resize((width*4, height*10), Image.NEAREST)
img.save("decoded.png")

