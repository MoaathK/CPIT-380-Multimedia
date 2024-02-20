from jes4py import *
# this code rotate the pic to the left
def rotateAPic():
    src = makePicture("salad.jpg")
    canvas = makeEmptyPicture(getWidth(src),getHeight(src))
    targetx = 0
    width = getWidth(src)
    for sourcex in range(0,getWidth(src)):
        targety = 0
        for sourcey in range(0,getHeight(src)):
            color = getColor(getPixel(src,sourcex,sourcey))

            setColor(getPixel(canvas,targety,width -targetx -1),color)
            targety = targety+1
        targetx = targetx+1
    
    explore(canvas)
    return canvas


rotateAPic()