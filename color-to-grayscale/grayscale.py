#!/usr/bin/env python

from PIL import Image


def rgbToGray(red, green, blue):
    gray = int(0.3*red + 0.59*green + 0.11*blue)
    return gray


"""
Do not touch above
"""


def rgbTupleToGrayTuple(RGBTuple):
    gray = 128  # Use the rgbToGray function here to calculate the gray color
    return (gray, gray, gray)


"""
Do not touch below
"""

housefile = open('../house.bmp')
houseimage = Image.open(housefile)

width = houseimage.size[0]
height = houseimage.size[1]
print('width: ' + str(width))
print('height: ' + str(height))

house = houseimage.load()

newhouseimage = Image.new('RGB', (width, height))
newhouse = newhouseimage.load()

for x in range(0, width):
    for y in range(0, height):
        newhouse[x, y] = rgbTupleToGrayTuple(house[x, y])

houseimage.show()
newhouseimage.show()
