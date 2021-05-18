'''
 14. Write a Python program to print a specified list after removing the 0th,
 4th and 5th elements.
 Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
 Expected Output : ['Green', 'White', 'Black']
'''

lis=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(lis)
lis.pop(5)
lis.pop(4)
lis.pop(0)
print(lis)
