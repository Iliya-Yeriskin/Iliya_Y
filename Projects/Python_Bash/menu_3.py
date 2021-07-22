#!/bin/python3

import os
from time import sleep
from random import randint


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
