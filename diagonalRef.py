from jes4py import *
def Diagonal(src):
    for sx in range(0,getWidth(src)):
        for sy in range(0,getHeight(src)):
          if (sx < sy):
            sPixel = getPixel(src,sx,sy)
            color = getColor(sPixel)
            tPixel = getPixel(src,sy,sx)
            setColor(tPixel,color)                    
    explore(src)

source = makePicture("salad.jpg")
Diagonal(source)
