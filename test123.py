from jes4py import*
def descreaseRedHalf(picture):
    pixels = getPixels(picture)
    for index in range(0,int(len(pixels)/2)):
        pixel = pixels[index]
        value = getRed(pixel)
        setRed(pixel,value*0.5)

#pic =makePicture("salad.jpg")
#descreaseRedHalf(pic)
aSound = makeSound("/Users/moath/Documents/Github/CPIT-380-Multimedia/Lab-8/Sounds/and.wav")

def increseVolume(sound):
    
    for sample in getSamples(sound):
        
        value = getSample(sample)
        setSample(sample,value*4)
    
    blockingPlay(sound)
    
    return sound

blockingPlay(aSound)
increseVolume(aSound)

