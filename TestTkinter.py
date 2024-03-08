
'''
r = tk.Tk()
r.geometry("500x300")
r.title('test')
button = tk.Button(r,text='Does it work?',width=25,command=r.destroy)
button.pack(side='bottom', padx=10, pady=10)
button.pack()
r.mainloop()
'''
#### this is How to get the value from a scrollbar ####
'''
def show_value():
    print(scale.get())

root = tk.Tk()
root.geometry("200x150")
# Create a Scale widget
scale = tk.Scale(root, from_=1, to=100, orient='horizontal')
scale.pack(padx=20, pady=20)

 #Button to print the current value of the scale
button = tk.Button(root, text="Get Value", command=show_value)
button.pack()

root.mainloop()

'''
from jes4py import*
import tkinter as tk
def scaleUpPic(entery):
    scaleFactor = entery.get()
    src = makePicture("salad.jpg")
    original_width = getWidth(src)
    original_height = getHeight(src)

    new_width = int(original_width * scaleFactor)
    new_height = int(original_height * scaleFactor)

    canvas = makeEmptyPicture(new_width,new_height)

    for x in range(new_width):
        for y in range(new_height):
            orgX = int(x/scaleFactor)
            orgY = int(y/scaleFactor)

            color = getColor(getPixel(src,orgX,orgY))
            setColor(getPixel(canvas,x,y),color)
    
    explore(canvas)
def getScaleValue():
    selectedValue = tk.scale.get()
    scaleUpPic(selectedValue)

def scaleDown():
    print("test")




def scaleUpXValue():
    Scale2 = tk.Tk()
    Scale2.geometry("500x300")
    Scale2.title('Scalling Up using number of X')
    labe2 = tk.Label(Scale2,text="Enter the X value wnat to scale-up").grid(row=0)
    e1 = tk.Entry(Scale2)
    e1.grid(row=0,column=1)
    
    
    
    button = tk.Button(Scale2 , text="Scale-Up", command=lambda: scaleUpPic(e1))
    button.grid(row=1, column=0, columnspan=2)
    buttonExit = tk.Button(Scale2 , text="Exit", command=Scale2.destroy)
    buttonExit.grid(row=2, column=0, columnspan=2)

    print("Test")



def scaleUpScrollbar():
    print("test")





def button_click():
    scaleup = tk.Tk()
    scaleup.geometry("500x300")
    scaleup.title('Scalling Up using number of X')
    labe2 = tk.Label(scaleup,text="Enter the X value wnat to scale-up").grid(row=0)
    e1 = tk.Entry(scaleup)
    e1.grid(row=0,column=1)
    label = tk.Label(r,text="Hello World!")
    label.pack(fill=tk.BOTH,expand=True)




r = tk.Tk()
r.geometry("500x300")
r.title('Main')
# this the lable and button to call the function scale up with scrollbar
lableScaleUpScroll = tk.Label(r,text="Scale Up using Scrollbar?").grid(row=0)
buttonScaleUpScroll = tk.Button(r,text="Click the button",command=scaleUpScrollbar).grid(row=0,column=1)
# this the lable and button to call the function scale up with X value
lableScaleUpXValue = tk.Label(r,text="Scale Up using X value?").grid(row=1)
buttonScaleUpXValue = tk.Button(r,text="Click the button",command=scaleUpXValue).grid(row=1,column=1)

# this is the lable and button to call the function scale Down using scrollbar
lableScaleDown = tk.Label(r,text="Scale Down using Scrollbar?").grid(row=2)
button = tk.Button(r,text="Click the button",command=scaleDown).grid(row=2,column=1)

r.mainloop()



'''
the user will chose between three options
1- do you wnat to scale down using scrollbar
2- do you want to scale up by number of X ex. 2X,3X
3- do you want to scal up using scrollbar

Steps:
1- window with three labels and the entry feild 
2- when clicking the button it should go to another widnow which will be the scrollbar or the 
'''
