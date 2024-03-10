from jes4py import*
#Example 2
program  = pickAFile()
print(program)

file = open(program,"rt")
contents = file.readlines()
print(contents)
file.close()
