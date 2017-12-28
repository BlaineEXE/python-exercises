#!/usr/bin/env python

from PIL import Image

housefile = open('house.bmp')
houseimage = Image.open(housefile)

width = houseimage.size[0]
height = houseimage.size[1]
print('width: ' + str(width))
print('height: ' + str(height))

house = houseimage.load()

newhouseimage = Image.new('RGB', (width, height))
newhouse = newhouseimage.load()

"""
Do not touch above
"""


def getBlurredValues(picture, x, y):
    # Do stuff
    return (128, 0, 255)  # placeholder return value


for x in range(0, width):
    for y in range(0, height):
        newhouse[x, y] = getBlurredValues(house, x, y)


"""
Do not touch below
"""

houseimage.show()
newhouseimage.show()
