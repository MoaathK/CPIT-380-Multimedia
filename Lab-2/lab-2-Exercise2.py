from jes4py import *

writeFile = open(r"c:\Users\m_h37\Desktop\CPIT-380-Multimedia\Lab-2\copy.txt","rt")
test = writeFile.read()


word = "This is Lab 2***"
lenghtOfWord = len(word)
if word in test:
    startIndex = test.find(word)
    extractTheString = test[startIndex: startIndex+lenghtOfWord]
    print(extractTheString)
else:
    print("Sentence not found")




