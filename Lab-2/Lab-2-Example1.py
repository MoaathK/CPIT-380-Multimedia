# Example 1
from jes4py import*
program  = pickAFile()
print(program)

file = open(program,"rt")
contents = file.read()
print(contents)
file.close()
