from jes4py import *
def MirrorUpToBot(source):
      mirrorPoint = int(getHeight(source) / 2)
      height = getHeight(source)
      for x in range(0,getWidth(source)):
        for y in range(0,mirrorPoint):
          topPixel = getPixel(source,x,y)
          bottomPixel = getPixel(source,x,height - y - 1)
          color = getColor(topPixel)
          setColor(bottomPixel,color)
      explore(source)
source = makePicture("salad.jpg")
MirrorUpToBot(source)
