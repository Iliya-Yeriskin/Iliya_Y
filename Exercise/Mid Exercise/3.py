'''
3. Write a Python program which accepts the user's first and last name and print them in reverse order
 with a space between them.
'''

first_name=input("Please enter your First Name: ")
last_name=input("Please enter your Last Name: ")
print("-------------------\nYour full name: "+str(first_name)+" "+str(last_name)+" backwards:")
print(first_name[::-1]+" "+last_name[::-1])
print(' '.join(first_name[::-1]+' '.join(last_name[::-1])))

