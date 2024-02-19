from jes4py import *
def myBlendPic_524():
  salad = makePicture("C:\Users\m_h37\Desktop\salad1.png")
  burger = makePicture("c:\Users\m_h37\Desktop\Test1.png")
  
  canvas = makeEmptyPicture(640,480)
  sourcex = 0
  for targetx in range(0,150):
    sourcey = 0
    for targety in range(0,getHeight(salad)):
      color = getColor(getPixel(salad,sourcex,sourcey))
      setColor(getPixel(canvas,targetx,targety),color)
      sourcey = sourcey+1
    sourcex = sourcex+1
  overlap = getWidth(salad)-150
  sourcex = 0
  for targetx in range(150,getWidth(salad)):
       sourcey =0
       for targety in range(0,getHeight(burger)):
          sPixel = getPixel(salad,sourcex+150,sourcey)
          bPixel = getPixel(burger,sourcex,sourcey)
          newRed = 0.50*getRed(sPixel) +0.5*getRed(bPixel)
          newGreen = 0.5*getGreen(sPixel) +0.5*getGreen(bPixel)
          newBlue = 0.5*getBlue(sPixel) + 0.5*getBlue(bPixel)
          color = makeColor(newRed,newGreen,newBlue)
          setColor(getPixel(canvas,targetx,targety),color)
          sourcey = sourcey+1
       sourcex =sourcex+1
  sourcex = overlap
  for targetx in range(150+overlap,getWidth(burger)-(150+overlap)):
    sourcey = 0
    for targety in range(0,getHeight(burger)):
      color = getColor(getPixel(burger,sourcex,sourcey))
      setColor(getPixel(canvas,targetx,targety),color)
      sourcey =sourcey+1
    sourcex =sourcex+1
      
  explore(canvas)
  return canvas
  
  
          
  