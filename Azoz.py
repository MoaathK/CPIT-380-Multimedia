def lighten():
  picture=makePicture("C:\Users\m_h37\Desktop\download.jpg")
  for x in range(0,getWidth(picture)):
    for y in range(0,getHeight(picture)):
      px = getPixel(picture,x,y)
      color = getColor(px)
      setColor(px,color)
  explore(picture)