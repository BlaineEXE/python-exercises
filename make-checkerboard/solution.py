#!/usr/bin/env python

from PIL import Image

# RGBTuple = (R, G, B)
# red = tuple[0], green = tuple[1], blue = tuple[2]
# (255, 255, 255) = white
# (0, 0, 0) = black

"""
Do not touch above
"""


def makeCheckerboard(boardimage):
    width = boardimage.size[0]
    height = boardimage.size[1]
    checkerboard = boardimage.load()
    for x in range(0, width):
        for y in range(0, height):
            inx = x % (width/4) < (width/8)  # % is modulo
            iny = y % (height/4) > (height/8)
            if inx ^ iny:  # ^ is xor
                checkerboard[x, y] = (255, 255, 255)


"""
Do not touch below
"""

checkerboard1image = Image.new('RGB', (32*8, 32*8))
checkerboard2image = Image.new('RGB', (64*8, 64*8))

makeCheckerboard(checkerboard1image)
makeCheckerboard(checkerboard2image)

checkerboard1image.show()
checkerboard2image.show()
