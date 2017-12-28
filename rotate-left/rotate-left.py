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


"""
Do not touch below
"""

houseimage.show()
newhouseimage.show()
