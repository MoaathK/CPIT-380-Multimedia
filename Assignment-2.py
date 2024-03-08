#Scaling Up a Picture
from jes4py import*
def scaleDown(src,scaleFactor):
    #scaleFactor = int(entery.get())
    src = makePicture("salad.jpg")
    newScaleF = (scaleFactor/100) +1
    new_width = int(getWidth(src) * (newScaleF/100))
    new_height = int(getHeight(src) * (newScaleF/100))

    canvas = makeEmptyPicture(new_width,new_height)

    for x in range(new_width):
        for y in range(new_height):
            orgX = int(x/(newScaleF/100))
            orgY = int(y/(newScaleF/100))

            color = getColor(getPixel(src,orgX,orgY))
            setColor(getPixel(canvas,x,y),color)
    explore(canvas)

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
scaleDown(source,70)

