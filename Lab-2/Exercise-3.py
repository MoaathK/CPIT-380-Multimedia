from jes4py import*
# this is required in the assignment
def writeToPyFile():
    writeFile  = open(r"lab-2/lab2.py","wt")
    writeFile.write("print (“Welcome to Jython programing language! This is Lab 2*** Happy to be here”)")
    writeFile.close()

    writeFile = open(r"lab-2/lab2.py","rt")
    test = writeFile.read()
    word = "This is Lab 2***"
    lenghtOfWord = len(word)
    if word in test:
        startIndex = test.find(word)
        extractTheString = test[startIndex: startIndex+lenghtOfWord]
        writeFile = open(r"lab-2/copy.txt","wt")
        writeFile.write(extractTheString)
    else:
      print("Sentence not found")

writeToPyFile()