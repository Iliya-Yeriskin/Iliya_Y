'''
11. Write a Python program to get a single string from two given strings,
 separated by a space and swap the first two characters of each string.
 Sample String : 'abc', 'xyz'
 Expected Result : 'xyc abz'
'''

a=input("Enter a 3 word string: ")
b=input("Enter a 2nd 3 word string: ")
print((b[0:2])+(a[2:3])+" "+(a[0:2])+(b[2:3]))

