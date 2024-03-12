from jes4py import*

writeFile  = open(r"lab2.py","wt")
writeFile.write("print (“Welcome to Jython programing language! This is Lab 2*** Happy to be here”)")

writeFile.close()

# now reading the file and copying it's content into another file

writeFile = open(r"lab2.py","rt")
test = writeFile.read()
writeFile = open(r"copy.txt","wt")
writeFile.write(test)
