#!bin/python3


from time import sleep
import os


print("Creating new file on Desktop....")
sleep(0.5)
os.system('cd V_Desktop ; touch my_details.txt')
os.system('''cd V_Desktop ; echo "Name: Iliya\nAge: 28\nGender: Male\nEmail: iliya@gmail.com" > my_details.txt''')
sleep(0.5)
print("File with your details created in V_Desktop folder")
