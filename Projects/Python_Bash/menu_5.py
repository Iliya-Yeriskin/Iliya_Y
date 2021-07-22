#!/bin/python3

import os
from time import sleep

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
