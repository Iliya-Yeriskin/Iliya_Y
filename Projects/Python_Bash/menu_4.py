#!/bin/python3

from time import sleep
import os


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
