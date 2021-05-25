



filename = '/Users/iliya/Desktop/Net4U/Python/L11-Files/test1.txt'
file = open(filename, "r")
my_string = file.read()
file.close()
print(my_string)
s_string = my_string.split(",")
print(s_string)
for i in s_string:
    print(i)
    file = open(filename, "a+")
    file.write("\n"+i)
    print(file.read())
    file.close()




