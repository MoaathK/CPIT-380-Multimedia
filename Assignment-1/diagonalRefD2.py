from jes4py import *
def DiagonalD2(src):
    
    for sx in range(getWidth(src) -1 , -1 , -1 ):
        
        for sy in range(getHeight(src) -1 , -1 , -1 ):
          if (sx + sy >= getWidth(src)):
            sPixel = getPixel(src , sx , sy)
            color = getColor(sPixel)
            tPixel = getPixel(src , getWidth(src) - sy - 1 , getHeight(src) - sx - 1)
            setColor(tPixel , color)             
    explore(src)

source = makePicture("salad.jpg")
DiagonalD2(source)
