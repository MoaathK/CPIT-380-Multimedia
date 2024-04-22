
from jes4py import*
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def converBackToPicture(data):
    height = len(data)
    width = len(data[0])

    newPicture = makeEmptyPicture(width, height)

    for x in range(height):
        for y in range(width):
            pixel = int(data[x][y])
            newColor = makeColor(pixel,pixel,pixel) 
            newPixel = getPixel(newPicture,x,y)
            setColor(newPixel,newColor)


    return newPicture            

def callNeighborhood(image,x,y):
    neighborhood = [
        image[x-1][y-1],image[x-1][y],image[x-1][y+1],
        image[x][y-1],image[x][y],image[x][y+1],
        image[x+1][y-1],image[x+1][y],image[x+1][y+1],
    ]
    return neighborhood
# Part 1
def simpleAverageFilter(image):
    newImage = []
    for x in range(getHeight(image)):
        row = [0] * getWidth(image)
        newImage.append(row)
    #copy = makeEmptyPicture(getWidth(image),getHeight(image))
    for x in range(1,getHeight(image)-1):
        for y in range(1,getWidth(image)-1):
            neighborhood = callNeighborhood(image,x,y)
            average = sum(neighborhood) /len(neighborhood)
            newImage[x][y] =average
    return newImage
# Part 2
def weightedAverage(image):
    height = getHeight(image)
    width = getWidth(image)

    weights = [
        [1,2,1],
        [2,4,2],
        [1,2,1]
    ]
    newImage = []
    for x in range(getHeight(image)):
        row = [0] * getWidth(image)
        newImage.append(row)

        for x in range(1,height-1):
            for y in range(1,width-1):
                weightSum = 0
                totalWeight = 0
                for i in range(3):
                    for j in range(3):
                        pixel = image[x-1 +i][y-1+j]
                        weight = weights[i][j]
                        weightSum = weightSum +pixel *weight
                        totalWeight = totalWeight +weightSum
                average = weightSum /totalWeight
                newImage[x][y] = average

    return newImage

# Part 3
def medianFilter(image):
    height = getHeight(image)
    width = getWidth(image)
    newImage = []
    for x in range(getHeight(image)):
        row = [0] * getWidth(image)
        newImage.append(row)

    for x in range(1,height-1):
        for y in range(1,width-1):
            neighborhood = callNeighborhood(image, x, y)
            median_value = sorted(neighborhood)[4]
            newImage[x][y] = median_value
    return newImage

# part 4 Min
def minFilter(image):
    height = getHeight(image)
    width = getWidth(image)
    newImage = []
    for x in range(getHeight(image)):
        row = [0] * getWidth(image)
        newImage.append(row)

    for x in range(1,height-1):
        for y in range(1,width-1):
            neighborhood = callNeighborhood(image, x, y)
            minValue = min(neighborhood)
            newImage[x][y] = minValue
    return newImage
# part 4 Max Filter
def maxFilter(image):
    height = getHeight(image)
    width = getWidth(image)
    newImage = []
    for x in range(getHeight(image)):
        row = [0] * getWidth(image)
        newImage.append(row)

    for x in range(1,height-1):
        for y in range(1,width-1):
            neighborhood = callNeighborhood(image, x, y)
            maxValue = max(neighborhood)
            newImage[x][y] = maxValue
    return newImage

# part 5 Laplacian Filter 
def laplacianFilter(image):
    kernal = [
        [0,-1,0],
        [-1,4,-1],
        [0,-1,0]        
    ]
    height = getHeight(image)
    width = getWidth(image)
    newImage = []
    for x in range(getHeight(image)):
        row = [0] * getWidth(image)
        newImage.append(row)
    
    for x in range(1,height-1):
            for y in range(1,width-1):
                laplcaianSum = 0
                for i in range(3):
                    for j in range(3):
                        pixel = image[x-1 +i][y-1+j]
                        weight = kernal[i][j]
                        laplcaianSum = laplcaianSum + pixel * weight
                
                newImage[x][y] = laplcaianSum
    return newImage

# Part 6 Sobel Filter
def sobalFilter(image):
    kernalX = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]
    kernalY = [
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ]
    height = getHeight(image)
    width = getWidth(image)
    newImage = []
    for x in range(getHeight(image)):
        row = [0] * getWidth(image)
        newImage.append(row)


    for x in range(1,height-1):
            for y in range(1,width-1):
                gardiX = 0
                gardiY = 0
                for i in range(3):
                    for j in range(3):
                        pixel = image[x-1 +i][y-1+j]
                        gardiX += pixel * kernalX[i][j]
                        gardiY += pixel * kernalY[i][j]

                gardientM = (gardiX**2 + gardiY**2)**0.5
                newImage[x][y] = gardientM
    
    return newImage


# part 7 Prewitt Filter
def prewittFilter(image):

    kernalX = [
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ]
    kernalY = [
        [-1, -1, -1],
        [0, 0, 0],
        [1, 1, 1]
    ]
    height = getHeight(image)
    width = getWidth(image)
    newImage = []
    for x in range(getHeight(image)):
        row = [0] * getWidth(image)
        newImage.append(row)


    for x in range(1,height-1):
            for y in range(1,width-1):
                gardiX = 0
                gardiY = 0
                for i in range(3):
                    for j in range(3):
                        pixel = image[x-1 +i][y-1+j]
                        gardiX += pixel * kernalX[i][j]
                        gardiY += pixel * kernalY[i][j]

                gardientM = (gardiX**2 + gardiY**2)**0.5
                newImage[x][y] = gardientM

    return newImage


# part 8 Robert Filter
def robertFilter(image):

    kernalX =[
        [1, 0],
        [0, -1]
    ]
    kernalY =[
        [0, 1],
        [-1, 0]
    ]
    height = getHeight(image)
    width = getWidth(image)
    newImage = []
    for x in range(getHeight(image)):
        row = [0] * getWidth(image)
        newImage.append(row)


    for x in range(1,height-1):
            for y in range(1,width-1):
                gardiX = 0
                gardiY = 0
                for i in range(3):
                    for j in range(3):
                        pixel = image[x-1 +i][y-1+j]
                        gardiX += pixel * kernalX[i][j]
                        gardiY += pixel * kernalY[i][j]

                gardientM = (gardiX**2 + gardiY**2)**0.5
                newImage[x][y] = gardientM

    return newImage
def buttonForPic(file_path_var,imageLabel):
    file_path = filedialog.askopenfilename(
        title="Choose a Picture",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")]
    )
    if file_path:
        file_path_var.set(file_path)  
        #print("Selected file:", file_path)
        
        
        image = Image.open(file_path)
        tkinter_image = ImageTk.PhotoImage(image)
        
        imageLabel.config(image=tkinter_image)
        imageLabel.image = tkinter_image

def Gui():
    root = tk.Tk()
    root.title("Choose a Picture")
    root.geometry("800x600")
    file_path_var = tk.StringVar()
    root.configure(bg="#222831")

    button_font = ("Arial", 14, "bold")
    chooseButton = tk.Button(root, text="Choose Picture", command=lambda: buttonForPic(file_path_var,imageLabel) , bg="#EEEEEE",fg="#78A083", font=button_font)
    chooseButton.pack(pady=20)
    imageLabel = tk.Label(root,bg="#222831")
    imageLabel.pack(pady=20) 
    
    #file_path_label = tk.Label(root, textvariable=file_path_var)
    #file_path_label.pack(pady=10)
    
    root.mainloop()
def main():
    # this will be the main
    #print("Test")
    Gui()


main()
