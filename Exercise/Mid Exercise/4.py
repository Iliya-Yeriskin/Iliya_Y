'''
4. Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java
Output : java
'''
file=input("Please enter a file full name: ")
type=file.split(".")
print("Your file type is: " + repr(type[-1]))

