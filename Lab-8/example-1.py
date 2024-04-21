from jes4py import*
#airplane
aSound = makeSound("C:\\Users\\m_h37\\Desktop\\Github\\CPIT-380-Multimedia\\Lab-8\\Sounds\\and.wav")
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

def main():
    #increseVolume(aSound)
    #increseVolume2(aSound)
    #increaseVolumeByRange(aSound)
    normalize(aSound)


main()
