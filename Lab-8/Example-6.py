from jes4py import*


def blind(sound1,sound2):
    length1 =  getNumSamples(sound1)
    length2 =  getNumSamples(sound2)
    high = max(length1,length2)
    less = min(length1,length2)

    newSound = makeEmptySound(high)
    if length2 >length1:
        test = sound2
        sound2 = sound1
        sound1 = test        

    for i in range(high):
        if i == less:
            break
        value1 = getSampleValueAt(sound1,i)
        value2 = getSampleValueAt(sound2,i)
        newValue = value1 + value2
        setSampleValueAt(newSound,i,newValue)
        


    return newSound

def main():
    file1 = pickAFile()
    file2 = pickAFile()

    sound1 = makeSound(file1)
    sound2 = makeSound(file2)
    blockingPlay(sound1)
    blockingPlay(sound2)

    sound3 = blind(sound1,sound2)

    blockingPlay(sound3)


main()

