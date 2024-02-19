
def copyHorse (): 
    src = makePicture("C:\Users\m_h37\Desktop\download.jpg")
    canvas = makeEmptyPicture(1000,1000)
    
    for sx in range(0,getWidth(src)):
     
      for sy in range(0,getHeight(src)):
          sourceP = getPixel(src,sx,sy)
          color = getColor(sourceP)
          targetP = getPixel(canvas,sy,getWidth(src)-sx -1)
          setColor(targetP,color)
      
    show(src)
    show(canvas)
    return canvas
