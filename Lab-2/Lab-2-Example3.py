from jes4py import*
writeFile  = open(r"c:\Users\m_h37\Desktop\CPIT-380-Multimedia\Lab-2\file1.txt","wt")
writeFile.write("Here is some text.")
writeFile.write("Here is some more.\n")
writeFile.write("And now we are done.\n\nTHE END.")

writeFile.close()

writeFile = open(r"c:\Users\m_h37\Desktop\CPIT-380-Multimedia\Lab-2\file1.txt","rt")
print(writeFile.read())
writeFile.close()