from jes4py import *

writeFile = open(r"copy.txt","rt")
test = writeFile.read()


word = "This is Lab 2***"
lenghtOfWord = len(word)
if word in test:
    startIndex = test.find(word)
    extractTheString = test[startIndex: startIndex+lenghtOfWord]
    print(extractTheString)
else:
    print("Sentence not found")




