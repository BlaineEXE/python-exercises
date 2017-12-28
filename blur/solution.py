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


def copyPixel(picture, x, y, width, height):
    if x < 0 or x >= width or y < 0 or y >= height:
        return None
    else:
        return picture[x, y]


def makeWorkingBox(picture, x, y, width, height, blur_radius):
    working_box = [[None]*(blur_radius*2+1) for i in range(blur_radius*2+1)]
    for x_offset in range(-blur_radius, blur_radius+1):
        for y_offset in range(-blur_radius, blur_radius+1):
            working_box[blur_radius+x_offset][blur_radius+y_offset] = \
                copyPixel(picture, x+x_offset, y+y_offset, width, height)
    return working_box


def extendWorkingBox(working_box):
    n = len(working_box)
    radius = (n-1)/2
    # Extend x right
    for x in range(radius+1, n):
        for y in range(0, n):
            if working_box[x][y] is None:
                working_box[x][y] = working_box[x-1][y]
    # Extend x left
    for x in range(radius-1, -1, -1):
        for y in range(0, n):
            if working_box[x][y] is None:
                working_box[x][y] = working_box[x+1][y]
    # Extend y down
    for x in range(0, n):
        for y in range(radius+1, n):
            if working_box[x][y] is None:
                working_box[x][y] = working_box[x][y-1]
    # Extend y up
    for x in range(0, n):
        for y in range(radius-1, -1, -1):
            if working_box[x][y] is None:
                working_box[x][y] = working_box[x][y+1]
    return working_box


def averageWorkingBox(working_box):
    total_red, total_green, total_blue = 0, 0, 0
    count = 0
    for row in working_box:
        for pixel in row:
            count += 1
            total_red += pixel[0]
            total_green += pixel[1]
            total_blue += pixel[2]
    return (total_red/count, total_green/count, total_blue/count)


def getBlurredPixel(picture, x, y, width, height, blur_radius):
    if x < 0 or y < 0 or x >= width or y >= height:
        raise Exception("out of bounds x=" + str(x) + " y=" + str(y))
    working_box = makeWorkingBox(picture, x, y, width, height, blur_radius)
    working_box = extendWorkingBox(working_box)
    return averageWorkingBox(working_box)


for x in range(0, width):
    for y in range(0, height):
        newhouse[x, y] = getBlurredPixel(house, x, y, width, height, 3)


"""
Do not touch below
"""

houseimage.show()
newhouseimage.show()
