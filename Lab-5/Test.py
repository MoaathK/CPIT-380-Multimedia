from jes4py import *

def swapBackToNew():
    picture = makePicture("C:\\Users\\m_h37\\Desktop\\Github\\CPIT-380-Multimedia\\Lab-5\\Picture11.png")
    backround = makePicture("C:\\Users\\m_h37\\Desktop\\Github\\CPIT-380-Multimedia\\Lab-5\\Picture2.png")
    newBackround = makePicture("C:\\Users\\m_h37\\Desktop\\Github\\CPIT-380-Multimedia\\Lab-5\\Picture3.png")
    #threshold = int(input("Enter the Threshold value: "))


    for px in getPixels(picture):
        x = getX(px)
        y = getY(px)
        backroundPx = getPixel(backround,x,y)
        pxColor = getColor(px)
        backColor = getColor(backroundPx)
        if distance(pxColor,backColor)<40.0:
            newColor = getColor(getPixel(newBackround,x,y))
            setColor(px,newColor)
    
    explore(picture)

swapBackToNew()
