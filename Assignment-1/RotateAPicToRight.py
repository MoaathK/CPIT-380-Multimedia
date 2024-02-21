from jes4py import *
# this code rotate the pic to the Right
def rotateAPic():
    src = makePicture("salad.jpg")
    canvas = makeEmptyPicture(getWidth(src),getHeight(src))
    
    for sourcex in range(0,getWidth(src)):
        
        for sourcey in range(0,getHeight(src)):
            color = getColor(getPixel(src, sourcex, sourcey))
            
            targetx = getHeight(src) - 1 - sourcey
            targety = sourcex
            setColor(getPixel(canvas, targetx, targety), color)
    explore(canvas)
    return canvas

rotateAPic()
