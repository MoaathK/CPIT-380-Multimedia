from jes4py import *

def Diagonal(src):
    for sx in range(0,getWidth(src)):
        for sy in range(0,getHeight(src)):
          if (sx > sy):#This condition reflect the upper tri to the lower tri
            # if we want to change so it reflect the lowee tri to the upper tri 
            # we can make the condtion to be (sx < sy)
            sPixel = getPixel(src,sx,sy)
            color = getColor(sPixel)
            tPixel = getPixel(src,sy,sx)
            setColor(tPixel,color)                    
    explore(src)



def DiagonalD2(src):
 
 for sx in range(getWidth(src) -1 , -1 , -1 ):
     for sy in range(getHeight(src) -1 , -1 , -1 ):
         if (sx + sy >= getWidth(src)):
            sPixel = getPixel(src , sx , sy)
            color = getColor(sPixel)
            tPixel = getPixel(src , getWidth(src) - sy - 1 , getHeight(src) - sx - 1)
            setColor(tPixel , color) 
 explore(src)

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


def reflectionVertical(source):
    mirrorPoint = int(getWidth(source) / 2)
    width = getWidth(source)
    for y in range(0,getHeight(source)):
        for x in range(0,mirrorPoint):
            leftPixel = getPixel(source,x,y) 
            rightPixel = getPixel(source,width - x - 1,y)
            color = getColor(leftPixel)
            setColor(rightPixel,color)
 
    explore(source)


def rotateAPicRight():
 src = makePicture("salad.jpg")
 canvas = makeEmptyPicture(getWidth(src),getHeight(src))
 for sourcex in range(0,getWidth(src)):
     for sourcey in range(0,getHeight(src)):
        color = getColor(getPixel(src, sourcex, sourcey))
        targetx = getHeight(src) - 1 - sourcey
        targety = sourcex
        setColor(getPixel(canvas, targetx, targety), color)
 explore(canvas)

def rotateAPic():
 src = makePicture("salad.jpg")
 canvas = makeEmptyPicture(getWidth(src),getHeight(src))
 targetx = 0
 width = getWidth(src)
 for sourcex in range(0,getWidth(src)):
     targety = 0
     for sourcey in range(0,getHeight(src)):
        color = getColor(getPixel(src,sourcex,sourcey))
        setColor(getPixel(canvas,targety,width -targetx -1),color)
        targety = targety+1
        targetx = targetx+1
 
 explore(canvas)


def D2TopToBot(src):
    for sx in range(getWidth(src) -1 , -1 , -1 ):
        for sy in range(getHeight(src) -1 , -1 , -1 ):
          if (sx + sy >= getWidth(src)):
            sPixel = getPixel(src , getWidth(src) - sy - 1 , getHeight(src) - sx - 1)
            color = getColor(sPixel)
            tPixel = getPixel(src , sx , sy)
            setColor(tPixel , color)
    explore(src)

def refVerticalRightToLeft(source):
    mirrorPoint = int(getWidth(source) / 2)
    width = getWidth(source)
    for y in range(0, getHeight(source)):
        for x in range(mirrorPoint, width):
            leftPixel = getPixel(source, x, y)
            rightPixel = getPixel(source, width - x - 1, y)
            color = getColor(leftPixel)
            setColor(rightPixel, color)
    explore(source)

def DiagonalBot(src):
    for sx in range(0,getWidth(src)):
        for sy in range(0,getHeight(src)):
          if (sx < sy):#This condition reflect the upper tri to the lower tri
            # if we want to change so it reflect the lowee tri to the upper tri 
            # we can make the condtion to be (sx < sy)
            sPixel = getPixel(src,sx,sy)
            color = getColor(sPixel)
            tPixel = getPixel(src,sy,sx)
            setColor(tPixel,color)                    
    explore(src)

def refHorizontalBotToTop(source):
    mirrorPoint = int(getHeight(source) / 2)
    height = getHeight(source)
    for x in range(0,getWidth(source)):
        for y in range(0,mirrorPoint):
            topPixel = getPixel(source,x,y)
            bottomPixel = getPixel(source,x,height - y - 1)
            color = getColor(bottomPixel)
            setColor(topPixel,color)
    explore(source)

def choose_and_display_function(image):

    print("\nImage Processing Functions:")
    print("1. Diagonal Top-Left to Bottom-Right (Upper Triangle)")
    print("2. Diagonal Top-Right to Bottom-Left (Lower Triangle)")
    print("3. Mirror Top Half to Bottom Half")
    print("4. Mirror Left Half to Right Half")
    print("5. Rotate 90 Degrees Clockwise")
    print("6. Rotate 90 Degrees Counter-Clockwise")
    print("7. Diagonal Bottom-Right to Top-Left (Upper Triangle)")
    print("8. Mirror Right Half to Left Half")
    print("9. Diagonal Top-Left to Bottom-Right (Lower Triangle)")
    print("10. Mirror Bottom Half to Top Half")
    print("0. Exit")

    while True:
        choice = input("\nEnter your choice (1-10 or 0 to exit): ")

        if choice == '0':
            print("Exiting...")
            return

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 10.")
            continue

        if choice < 0 or choice > 10:
            print("Invalid choice. Please enter a number between 0 and 10.")
            continue


        source_image = makePicture(image)

        # Execute the chosen function and display the result
        if choice == 1:
            Diagonal(source_image)
        elif choice == 2:
            DiagonalD2(source_image)
        elif choice == 3:
            MirrorUpToBot(source_image)
        elif choice == 4:
            reflectionVertical(source_image)
        elif choice == 5:
            rotateAPicRight()
        elif choice == 6:
            rotateAPic()  
        elif choice == 7:
            D2TopToBot(source_image)
        elif choice == 8:
            refVerticalRightToLeft(source_image)
        elif choice == 9:
            DiagonalBot(source_image)
        elif choice == 10:
            refHorizontalBotToTop(source_image)

        # Display the processed image
        explore(source_image)

        print("\nImage processed successfully.")

choose_and_display_function("salad.jpg")