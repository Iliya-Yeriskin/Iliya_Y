#File Handling
#'w' - for write in a file
#'r' - for reading file
#'r+' - for read and write(overwrite) a file
#'a' - append to add ('w') to a file
#'a+' - append and reads a file


filename = '/Users/iliya/Desktop/Net4U/Python/L11-Files/test1.txt'
file = open(filename, "a")
file.write("192.168.1.3\n192.168.1.4")
file.close()
file = open(filename, "r")
print(file.read())
file.close()


#file = open(filename, "w")
#file.write("192.168.1.3\n192.168.1.4")
#file.close()


#file = open(filename, "r+")
#print(file.read())
#file.write("192.168.1.1\n192.168.1.2")
#print(file.read())
#file.close()


#file = open(filename, "r")
#print(file.read())
#file.close()
