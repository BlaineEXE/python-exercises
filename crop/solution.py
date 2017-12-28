#!/usr/bin/env python

from PIL import Image

housefile = open('house.bmp')
houseimage = Image.open(housefile)

width = houseimage.size[0]
height = houseimage.size[1]
print('width: ' + str(width))
print('height: ' + str(height))

house = houseimage.load()

newhouseimage = houseimage.copy()
newhouse = newhouseimage.load()

"""
Do not touch above
"""


def crop(pictureimage, upperLeftPixel, lowerRightPixel):
    width = pictureimage.size[0]
    height = pictureimage.size[1]
    picture = pictureimage.load()
    for x in range(0, width):
        for y in range(0, height):
            if(x < upperLeftPixel[0] or x > lowerRightPixel[0] or
                    y < upperLeftPixel[1] or y > lowerRightPixel[1]):
                picture[x, y] = (255, 255, 255)


"""
Do not touch below
"""

upperLeft = (146, 90)
lowerRight = (width-47, height-58)
crop(newhouseimage, upperLeft, lowerRight)

houseimage.show()
newhouseimage.show()
