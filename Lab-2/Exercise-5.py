from jes4py import*

def readLines():
    writeFile = open(r"lab-2/Ex4.txt","rt")
    Lines3 = []
    for s in range(3):
        line = writeFile.readline()
        if line:
            Lines3.append(line.rstrip())
        else:
            break
    
    for l in Lines3:
        print(l)


readLines()