from jes4py import*

def copyImge(src):
    width = getWidth(src)
    height = getHeight(src)
    copy = makeEmptyPicture(width,height)
    targetX = 0
    for sourceX in range(0,getWidth(src)):
        targetY = 0
        for sourceY in range(0,getHeight(src)):
            color = getColor(getPixel(src,sourceX,sourceY))

            setColor(getPixel(copy,targetY,width -targetX -1),color)
            targetY = targetY+1
        targetX = targetX+1
    return copy
    
def simple(src):
    width = getWidth(src)
    height = getHeight(src)
    copy = copyImge(src)
    for v in range(1,height-2):
        for u in range(1, width -2):
            sum = 0
            for j in range(-1,1):
                for i in range(-1,1):
                    p =getPixel(copy,u+i,v+j)
                    sum = sum +p
            
            #q = (int) math.round(sum/9.0)
            
