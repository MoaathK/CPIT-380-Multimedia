import matplotlib.pyplot as plt
from jes4py import *
import pandas as pn
import numpy as np
# Work steps
# 1- loop throw the Pic and get each color intesity in their arrays
# 2- Visual the three Arrays
# 3- then do the algorithm 
# 4- then explore the two pictures 
def histogramEqualization(hist):
    cdf = np.cumsum(hist)
    cdf_normalized = cdf * 255 / cdf[-1]
    new_values = np.round(cdf_normalized).astype(np.uint8)
    return new_values

def pictureToArray(picture):
    width, height = getWidth(picture), getHeight(picture)
    array = np.zeros((height, width, 3), dtype=np.uint8)
    for x in range(width):
        for y in range(height):
            pixel = getPixel(picture, x, y)
            array[y, x] = [getRed(pixel), getGreen(pixel), getBlue(pixel)]
    return array



def calculateColor(img):
    src = makePicture(img)
    histR = [0] * 256
    histG = [0] * 256
    histB = [0] * 256
    count = 0 
    for x in range(src.getWidth()):
        for y in range(src.getHeight()):
            img = getPixel(src,x,y)
            rColor = getRed(img)
            gColor = getGreen(img)
            bColor = getBlue(img)
            histR[rColor] +=1
            histG[gColor] +=1
            histB[bColor] +=1
            count += 1


    # visualizing the RGB histogram
    plt.plot(range(256), histR, color='red')
    plt.xlabel('red value',)
    plt.ylabel('Frequency')
    plt.title('Red Histogram')
    plt.xticks(np.arange(0, 261, step=20))
    plt.show()


    plt.plot(range(256), histG, color='green')
    plt.xlabel('green value',)
    plt.ylabel('Frequency')
    plt.title('green Histogram')
    plt.xticks(np.arange(0, 261, step=20))
    plt.show()


    plt.plot(range(256), histB, color='blue')
    plt.xlabel('blue value',)
    plt.ylabel('Frequency')
    plt.title('blue Histogram')
    plt.xticks(np.arange(0, 261, step=20))
    plt.show()

    # performing the Equalization to the three colors
    redColor = histogramEqualization(histR)
    blueColor = histogramEqualization(histB)
    greenColor = histogramEqualization(histG)
    newImage = makeEmptyPicture(getWidth(src),getHeight(src))
    for x in range(src.getWidth()):
        for y in range(src.getHeight()):
            pixel = getPixel(src, x, y)
            newR, newG, newB = redColor[getRed(pixel)], greenColor[getGreen(pixel)], blueColor[getBlue(pixel)]
            newColor = makeColor(newR,newG,newB)
            setColor(getPixel(newImage,x,y),newColor)


    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    ax[0].imshow(pictureToArray(src))  
    ax[0].set_title('Before')
    ax[0].axis('off') 
    ax[1].imshow(pictureToArray(newImage))
    ax[1].set_title('After')
    ax[1].axis('off')
    plt.show()
    
    


    


image = "C:\\Users\\m_h37\\Desktop\\Github\\CPIT-380-Multimedia\\salad.jpg"
calculateColor(image)
