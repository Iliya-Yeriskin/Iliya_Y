#Lists

new_list=[1,2,28,6.6,"iliya yeriskin"]
print(new_list)
print("My name is: " + new_list[4])
print("My age is: " + str(new_list[2]))
'''
'''
my_list1=new_list*2
print(my_list1)
'''
'''
#making from list from a string and string from a list .join / .split commands
my_list2=list("1234567")
print(my_list2)
my_string=''.join(my_list2)
print(my_string)
my_list3=my_string.split()
print(my_list3)
'''
'''
#length of string or list "len" command
my_list=["hello",1,66.6,"Iliya",55,77.7]
print("The length is: " + str(len(my_list)))
my_str="12324354365467657565233"
print("The length is: " + str(len(my_str)))
#.append adds to the end of the list
my_list.append("wow")
my_list.append("world")
print(my_list)
print("The new length is: " + str(len(my_list)))
#.insert is adding to the list in a specific cell
my_list.insert(7,2) #in cell 7 add the number 2
print(my_list)
#.pop deletes the last cell in the list or you can decide what cell to delete
my_list.pop(7)  #deletes the data from cell 7
print(my_list)
#true or false in list
list2=["ebay","google","facebook","apple"]
print("ebay" in list2)
