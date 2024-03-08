
from jes4py import*
import tkinter as tk
# this method is  for scaling an image using X Value
def scaleUpPicByValue(entery):
    scaleFactor = int(entery.get())
    src = makePicture("salad.jpg")

    new_width = int(getWidth(src) * scaleFactor)
    new_height = int(getHeight(src) * scaleFactor)

    canvas = makeEmptyPicture(new_width,new_height)

    for x in range(new_width):
        for y in range(new_height):
            orgX = int(x/scaleFactor)
            orgY = int(y/scaleFactor)

            color = getColor(getPixel(src,orgX,orgY))
            setColor(getPixel(canvas,x,y),color)
    
    explore(canvas)

# this method is for the window that shows the scale Up Using X value
def scaleUpXValue():
    Scale2 = tk.Tk()
    Scale2.geometry("500x300")
    Scale2.title('Scalling Up using number of X')
    labe2 = tk.Label(Scale2,text="Enter the X value wnat to scale-up").grid(row=0)
    e1 = tk.Entry(Scale2)
    e1.grid(row=0,column=1)
    button = tk.Button(Scale2 , text="Show Pic", command=lambda: scaleUpPicByValue(e1))
    button.grid(row=2, column=0, columnspan=2)
    buttonExit = tk.Button(Scale2 , text="Exit", command=Scale2.destroy)
    buttonExit.grid(row=4, column=0, columnspan=2)

def getScale(scale,x):
    selectValue = int(scale.get())
    if x == 1:
        #call the scale Up method
        scaleUpPicScaleBar(selectValue)
    elif x == 2 and selectValue !=100:
        scaleDownScaleBar(selectValue)

# this method is for scalling the img using scale bar
def scaleUpPicScaleBar(scaleFactor):
    src = makePicture("salad.jpg")
    original_width = getWidth(src)
    original_height = getHeight(src)
    #newScaleF = (scaleFactor/100)+1
    new_width = int(original_width * ( (scaleFactor/100) +1 ) )
    new_height = int(original_height * ( (scaleFactor/100) +1 ) )

    canvas = makeEmptyPicture(new_width,new_height)

    for x in range(new_width):
        for y in range(new_height):
            orgX = int(x/((scaleFactor/100)+1))
            orgY = int(y/((scaleFactor/100)+1))

            color = getColor(getPixel(src,orgX,orgY))
            setColor(getPixel(canvas,x,y),color)
    
    explore(canvas)
# this function is for the window that displays the scale bar for the user
def scaleUpScrollbar():
    scale1 = tk.Tk()
    scale1.geometry("500x300")
    scale1.title('Scalling Up using scale')
    labelScale = tk.Label(scale1, text="Using this scroll choice the value you want to scale Up").grid(row=0)

    # now implementing the scale Method
    scale = tk.Scale(scale1 , from_=1 ,to=100,orient='horizontal')
    scale.grid(row=3)
    button = tk.Button(scale1, text="Show Pic" ,command=lambda: getScale(scale,1))
    button.grid(row=6)

    buttonExit = tk.Button(scale1 , text="Exit", command=scale1.destroy)
    buttonExit.grid(row=9, column=0, columnspan=2)       


# this function is for the logic operation of scaling an img down using scale bar
def scaleDownScaleBar(scaleFactor):
    
    src = makePicture("salad.jpg")
    if scaleFactor == 100:
        exit

    newScaleF = 100-scaleFactor
    new_width = int(getWidth(src) * (newScaleF/100))
    new_height = int(getHeight(src) * (newScaleF/100))

    canvas = makeEmptyPicture(new_width,new_height)

    for x in range(new_width):
        for y in range(new_height):
            orgX = int(x/(newScaleF/100))
            orgY = int(y/(newScaleF/100))

            color = getColor(getPixel(src,orgX,orgY))
            setColor(getPixel(canvas,x,y),color)
    explore(canvas)

# this function is for the window that displays the scale down scale bar
def scaleDown():
    scaleD = tk.Tk()
    scaleD.geometry("500x300")
    scaleD.title('Scalling Down using scale')
    labelScale = tk.Label(scaleD, text="Using this scroll choice the value you want to scale Down").grid(row=0)

    # now implementing the scale Method
    scale = tk.Scale(scaleD , from_=1 ,to=100,orient='horizontal')
    scale.grid(row=4)

    button = tk.Button(scaleD, text="Show Pic" ,command=lambda: getScale(scale,2))
    button.grid(row=6)

    buttonExit = tk.Button(scaleD , text="Exit", command=scaleD.destroy)
    buttonExit.grid(row=8, column=0, columnspan=2)    







# here start the main for the project
r = tk.Tk()
r.geometry("500x300")
r.title('Main')
# this the lable and button to call the function scale up with scrollbar
lableScaleUpScroll = tk.Label(r,text="Scale Up using Scale Bar?").grid(row=0)
buttonScaleUpScroll = tk.Button(r,text="Click the button",command=scaleUpScrollbar).grid(row=0,column=1)


# this the lable and button to call the function scale up with X value
lableScaleUpXValue = tk.Label(r,text="Scale Up using X value?").grid(row=2)
buttonScaleUpXValue = tk.Button(r,text="Click the button",command=scaleUpXValue).grid(row=2,column=1)


# this is the lable and button to call the function scale Down using scrollbar
lableScaleDown = tk.Label(r,text="Scale Down using Scale Bar?").grid(row=4)
button = tk.Button(r,text="Click the button",command=scaleDown).grid(row=4,column=1)

r.mainloop()



'''
the user will chose between three options
1- do you wnat to scale down using scrollbar
2- do you want to scale up by number of X ex. 2X,3X
3- do you want to scal up using scrollbar

Steps:
1- window with three labels and the entry feild 
2- when clicking the button it should go to another widnow which will be the Scale Bar or the 
'''
