from jes4py import*

def simpleAverageSound(sound,windowSize):

    length = getNumSamples(sound)
    newSound = makeEmptySound(length)

    for i in range(length):
        start = max(0, i - windowSize //2)
        end = min(length, i +windowSize//2 +1)

        currentValue=[]
        for j in range(start, end):
            currentValue.append(getSampleValueAt(sound,j))

        newAverage = sum(currentValue) / len(currentValue)
        setSampleValueAt(newSound,i,newAverage)
    return newSound




sound = makeSound("Lab-7\\frequent.wav")
window_size = 10  
simpleAverageNewSound = simpleAverageSound(sound,window_size)
blockingPlay(simpleAverageNewSound)

