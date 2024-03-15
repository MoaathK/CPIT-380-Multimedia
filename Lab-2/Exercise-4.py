from jes4py import*
def findWord():

    writeFile = open(r"lab-2/Ex4.txt","rt")
    test = writeFile.read()
    sentences = test.split('.')

    word = input("Enter the String you want to search: ")
    
    check = False
    for sentence in sentences:
        if word in sentence:
           print("Found the word in sentecne " , sentence.strip())
           check = True
           break
    if not check:
        print("Word is not in the File")

findWord()