filename = '/Users/iliya/Desktop/Net4U/Python/L11-Files/test1.txt'
file = open(filename, "r")
lines = file.readlines()
file.close()
print(lines[3]+lines[4])
