#!/usr/bin/env python

from PIL import Image

housefile = open('../house.bmp')
houseimage = Image.open(housefile)

width = houseimage.size[0]
height = houseimage.size[1]
print('width: ' + str(width))
print('height: ' + str(height))

house = houseimage.load()

newhouseimage = Image.new('RGB', (width, height))
newhouse = newhouseimage.load()

# RGBTuple = (R, G, B)
# red = tuple[0], green = tuple[1], blue = tuple[2]

"""
Do not touch above
"""

for x in range(0, width):
    for y in range(0, height):
        pixel = house[x,y]
        newhouse[x,y] = (pixel[0], 0, pixel[2])


"""
Do not touch below
"""

houseimage.show()
newhouseimage.show()
