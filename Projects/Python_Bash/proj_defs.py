#!bin/python3


from time import sleep
import os
from random import randint

def details():
	print("Creating new file on Desktop....")
	sleep(0.5)
	os.system('cd V_Desktop ; touch my_details.txt')
	name=input("Enter your Name: ")
	age=input("Enter your Age: ")
	email=input("Enter your Email: ")
	os.system('''cd V_Desktop ; echo "Name: {}\nAge: {}\nEmail: {}" > my_details.txt'''.format(name,age,email))
	sleep(0.5)
	print("File with your details created in V_Desktop folder")


def count200():
	print("Starting the count to 200..")
	for i in range(1,201):
		print(i)
		sleep(0.5)
	print("Done counting to 200.")


def cubes():
	cube1=randint(1,6)
	cube2=randint(1,6)
	print("Rolling the cubes...")
	sleep(2)
	print("Checking if the cubes are the same:")
	sleep(1)
	if cube1 == cube2:
		print("Cube1 = "+str(cube1)+"\nCube2 = "+str(cube2))
		sleep(1)
		print("You lucky! your cubes are the same")
	else:
		print("Cube1 = "+str(cube1)+"\nCube2 = "+str(cube2))
		sleep(1)
		print("Sorry, the Cubes are different")


def compress():
	print("Creating 10 Compressed files in 1 tgz archive...")
	for i in range(1,11):
		os.system('cd V_Desktop ; touch {}.txt'.format(i))
		os.system('cd V_Desktop ; echo "{}.txt" >> mylist.txt'.format(i))
		print("Created File: "+str(i))
		sleep(0.4)
	print("Done creating all files, Now will compress them to tgz archive..")
	sleep(0.5)
	os.system('cd V_Desktop ; tar -zcf compressed.tgz -T mylist.txt ; rm 1.txt 2.txt 3.txt 4.txt 5.txt 6.txt 7.txt 8.txt 9.txt 10.txt')
	print("Done Compressing the file into archive\nNow will show the content of the folder(V_Desktop):")
	sleep(1)
	os.system('cd V_Desktop ; ls -lhtr')



def new_users():
	print("Creating 2 Users...")
	user1=input("Please Enter Username1 ID: ")
	user2=input("Please Enter Username2 ID: ")
	os.system('sudo adduser {} ; sudo adduser {}'.format(user1,user2))
	print("Useres Created\nNow adding them to sudo Group...")
	sleep(1)
	os.system('sudo usermod -aG sudo {} ; sudo usermod -aG sudo {}'.format(user1,user2))
	print("Done Adding new users to sudo Group,\nUser1 ID: ")
	os.system('id {}'.format(user1))
	print("User2 ID: ")
	os.system('id {}'.format(user2))
