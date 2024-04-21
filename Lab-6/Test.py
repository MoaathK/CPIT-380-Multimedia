
from jes4py import*

def callNeighborhood(image,x,y):
    neighborhood = [
        image[x-1][y-1],image[x-1][y],image[x-1][y+1],
        image[x][y-1],image[x][y],image[x][y+1],
        image[x+1][y-1],image[x+1][y],image[x+1][y+1],
    ]
    return neighborhood

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

        for x in range(1,height):
            for y in range(1,width):
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