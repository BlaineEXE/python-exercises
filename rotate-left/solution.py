#!/usr/bin/env python

from PIL import Image

housefile = open('house.bmp')
houseimage = Image.open(housefile)

width = houseimage.size[0]
height = houseimage.size[1]
print('width: ' + str(width))
print('height: ' + str(height))

house = houseimage.load()

newhouseimage = Image.new('RGB', (height, width))  # height and width switched
newhouse = newhouseimage.load()

"""
Do not touch above
"""

for x in range(0, width):
    for y in range(0, height):
        newhouse[y, x] = house[width-x-1, y]


"""
Do not touch below
"""

houseimage.show()
newhouseimage.show()
