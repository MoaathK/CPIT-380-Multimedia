from jes4py import*

writeFile  = open(r"c:\Users\m_h37\Desktop\CPIT-380-Multimedia\Lab-2\lab2.py","wt")
writeFile.write("print (“Welcome to Jython programing language! This is Lab 2*** Happy to be here”)")

writeFile.close()

# now reading the file and copying it's content into another file

writeFile = open(r"c:\Users\m_h37\Desktop\CPIT-380-Multimedia\Lab-2\lab2.py","rt")
test = writeFile.read()
writeFile = open(r"c:\Users\m_h37\Desktop\CPIT-380-Multimedia\Lab-2\copy.txt","wt")
writeFile.write(test)
