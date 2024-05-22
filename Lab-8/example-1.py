from jes4py import*
#airplane
aSound = makeSound("/Users/moath/Documents/Github/CPIT-380-Multimedia/Lab-8/Sounds/about.wav")
def example1():
    print(aSound)

    #blockingPlay(aSound)
    print("Sample value at specifix index")
    print( getSampleValueAt(aSound,4))


    # Change Value at index 4 to 12
    print(getSampleValueAt(aSound,4))
    setSampleValueAt(aSound,4,12)
    print(getSampleValueAt(aSound,4))

        # get the sampling rate
    print(getSamplingRate(aSound))


def increseVolume(sound):
    for sample in getSamples(sound):
        value = getSampleValue(sample)
        setSampleValue(sample,value*4)
    
    blockingPlay(sound)
    return sound

def increseVolume2(sound):
    Samples = getSamples(sound)
    for index in range(len(Samples)):
        sample = Samples[index]
        value = getSampleValue(sample)
        setSampleValue(sample,value*2)

def increaseVolumeByRange(sound):
    for index in range(0,getLength(sound)):
        value = getSampleValueAt(sound,index)
        setSampleValueAt(sound, index,value*2)
    blockingPlay(sound)
# 
def normalize(sound):
    #incresedSound = increseVolume(sound,10)
    blockingPlay(sound)
    largest = 0
    for s in getSamples(sound):
        largest = max(largest,getSampleValue(s))
    multiplier = 32767.0/largest
    print("Largest Sample value in original sound was ",largest)
    print("Multiplier is",multiplier)

    for s in getSamples(sound):
        louder = multiplier * getSampleValue(s)
        setSampleValue(s,louder)

    blockingPlay(sound)

# this will increase the sound or decrease it by the factor which the user will provide it.
def changeVolume(sound,factor):
    for sample in getSamples(sound):
        value = getSampleValue(sample)
        setSampleValue(sample,value*factor)
    
    blockingPlay(sound)



def merge():
    people = makeSound(getMediaPath("/Users/moath/Documents/Github/CPIT-380-Multimedia/Lab-8/Sounds/people.wav"))
    outside = makeSound(getMediaPath("/Users/moath/Documents/Github/CPIT-380-Multimedia/Lab-8/Sounds/outside.wav"))
    target = makeEmptySound(getSamples(people)+getSamples(outside) + 3,)
    
    index = 0
    for source in getSamples(people):
        value = getSampleValueAt(people,source)
        setSampleValueAt(target,index,value)
        index += 1
    for source in range(0, int(0.1 * getSamplingRate(target))): ## putting space between the two words
        setSampleValueAt(target,index,0)
        index +=1
    for source in getSamples(outside):
        value = getSampleValueAt(outside,source)
        setSampleValueAt(target,index,value)
        index +=1
    
    normalize(target)
    blockingPlay(target)

        
def reverse(sound): # this function do reversing to sounds 
    target = makeEmptySound(getLength(sound))
    sourceIndex = getLength(sound)-1
    for targetIndex in range(0,getLength(target)):
        value = getSampleValueAt(sound,sourceIndex)
        setSampleValueAt(target,targetIndex,value)
        sourceIndex = sourceIndex-1

def mirroring(sound): # this function should perform a mirroring to sounds
    length = getLength(sound)
    mirrorPoint = length/2
    for index in range(0,mirrorPoint):
        left = getSampleObjectAt(sound,index)
        right = getSampleObjectAt(sound,length-index -1)
        value = getSampleValue(left)
        setSampleValue(right,value)


def echo(soundPath,deley): # this function will make the sound have echo
    sound1 = makeSound(soundPath)
    sound2 = makeSound(soundPath)
    for index in range(deley,getLength(sound1)):
        echo = 0.6 * getSampleValueAt(sound2,index-deley)
        combo = getSampleValueAt(sound1,index ) +echo
        setSampleValueAt(sound1,index,combo)

    
def main():
    #increseVolume(aSound)
    #increseVolume2(aSound)
    #increaseVolumeByRange(aSound)
    normalize(aSound)
    #merge()


main()
