from jes4py import *

def edge(picture):
    all = getPixels(picture)
    for index in range(0,len(all)-1):
        this = all[index]
        next = all[index+1]
        tsum = getRed(this) + getBlue(this) + getGreen(this)
        nsum = getRed(next) + getBlue(next) + getGreen(next)

        lum = abs(tsum-nsum)
        setColor(this,makeColor(lum,lum,lum))


def neg(pic):
    for p in getPixels(pic):
        nuColor = makeColor(255-getRed(p),255-getGreen(p), 255-getBlue(p))
        setColor(p,nuColor)

def main():
    salad = makePicture("/Users/moath/Documents/Github/CPIT-380-Multimedia/salad.jpg")
    edge(salad)
    neg(salad)
    explore(salad)



main()