'''
Create 2 variables: string of your full name and string of your email.
Create variabble of your age (int)
print all of them to the screen
then print your name from the end to the beginning and print it only with age*3.
then check if your name is stored inside this full string:
"idan ben dudu yuval shimon yael gal adam shahar yana"
'''

n="iliya yeriskin"
e="iliya@gmail.com"
a=28
#print my name+email+age
print(n + "\n" + e +"\n" + str(a))
#print my name backward and age*3
print(n[::-1] + "\n" + str(a*3))
#check if my name is in the string:
list="idan ben dudu yuval shimpn yael gal adam shahar yana"
print("iliya" in list)







