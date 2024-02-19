from jes4py import *
def Diagonal(src):
    for sx in range(0,getWidth(src)):
        for sy in range(0,getHeight(src)):
          if (sx + sy < getHeight(src)):#This condition reflect the upper tri to the lower tri
            # if we want to change so it reflect the lowee tri to the upper tri 
            # we can make the condtion to be (sx < sy)
            sPixel = getPixel(src,sx,sy)
            color = getColor(sPixel)
            tPixel = getPixel(src,sy,sx)
            setColor(tPixel,color)                    
    explore(src)

source = makePicture("salad.jpg")
Diagonal(source)
