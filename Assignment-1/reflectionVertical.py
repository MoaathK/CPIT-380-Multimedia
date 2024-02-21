from jes4py import *

def reflectionVertical(source):
    mirrorPoint = int(getWidth(source) / 2)
    width = getWidth(source)
    for y in range(0,getHeight(source)):
        for x in range(0,mirrorPoint):
            leftPixel = getPixel(source,x,y) 
            rightPixel = getPixel(source,width - x - 1,y)
            color = getColor(leftPixel)
            setColor(rightPixel,color)
    
    explore(source)
source = makePicture("salad.jpg")
reflectionVertical(source)
