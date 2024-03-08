#Scaling Up a Picture
from jes4py import*
def scaleUpPic(src,scaleFactor):
    original_width = getWidth(src)
    original_height = getHeight(src)

    new_width = int(original_width * scaleFactor)
    new_height = int(original_height * scaleFactor)

    canvas = makeEmptyPicture(new_width,new_height)

    for x in range(new_width):
        for y in range(new_height):
            orgX = int(x/scaleFactor)
            orgY = int(y/scaleFactor)

            color = getColor(getPixel(src,orgX,orgY))
            setColor(getPixel(canvas,x,y),color)
    
    explore(canvas)


source = makePicture("salad.jpg")
scaleUpPic(source,2)

