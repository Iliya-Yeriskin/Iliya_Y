#!/bin/python3

from time import sleep
import os
from proj_defs import *

e = "n"
while e == "n":
	print("Hello Please choose an option from the Menu\nMenu:\n1.Create a new file in V_Desktop with your details")
	print("2.Run a loop that count to 200\n3.Random 2 cubes and check if they are equal or not")
	print("4.Run loop from 1-10 to create 10 files and compress them to tgz file in V_Desktop")
	print("5.Create 2 Users and put themn in SUDO Group")
	choise = input("Enetr your choise: ")
	if choise == "1":
		details()
	elif choise == "2":
		count200()
	elif choise == "3":
		cubes()
	elif choise == "4":
		compress()
	elif choise == "5":
		new_users()
	else:
		print("Please Enter 1-5 ONLY!!")
	while e != "n" or e != "y":
		e = input("Do you want to Exit (y/n)?")
		if e == "n":
			print("______________________\nReturning to Menu\n______________________")
			sleep(1)
			break
		elif e == "y":
			print("________________________\nThank you & Byebye.")
			break
		else:
			print("Enter y/n ONLY!\nEnetr Again: ")
			continue
