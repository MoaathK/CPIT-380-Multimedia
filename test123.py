from jes4py import*
def descreaseRedHalf(picture):
    pixels = getPixels(picture)
    for index in range(0,int(len(pixels)/2)):
        pixel = pixels[index]
        value = getRed(pixel)
        setRed(pixel,value*0.5)

pic =makePicture("salad.jpg")
descreaseRedHalf(pic)
