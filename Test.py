def mirrorVertical(src):


    for sx in range(0,getWidth(src)):
        for sy in range(0,getHeight(src)):
          if (sx > sy):
            sPixel = getPixel(src,sx,sy)
            color = getColor(sPixel)
            tPixel = getPixel(src,sy,sx)
            setColor(tPixel,color)
          
          
          
    show(src)
    explore(src)


