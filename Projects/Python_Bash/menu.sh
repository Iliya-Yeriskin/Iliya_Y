#!/bin/bash


e="n"
while [ $e == "n" ]
do
	echo -e "Hello Please choose an option from the Menu\nMenu:\n1.Create a new file in V_Desktop with your details"
	echo -e "2.Run a loop that count to 200\n3.Random 2 cubes and check if they are equal or not"
	echo -e "4.Run loop from 1-10 to create 10 files and compress them to tgz file in V_Desktop"
	echo -e "5.Create 2 Users and put themn in SUDO Group"
	read choise
	if [ $choise == 1 ]
	then
		echo "You choose 1"
		sleep 1
		python3 menu_1.py
	elif [ $choise == 2 ]
	then
		echo "You choose 2"
                sleep 1
		python3 menu_2.py
	elif [ $choise == 3 ]
	then
		echo "You choose 3"
                sleep 1
        	python3 menu_3.py
	elif [ $choise == 4 ]
	then
		echo "You choose 4"
                sleep 1
        	python3 menu_4.py
	elif [ $choise == 5 ]
	then
		echo "You choose 5"
                sleep 1
        	python3 menu_5.py
	else
		echo "Please Enter 1-5 ONLY!!!"
	fi
	echo "Do you want to Exit? (y/n)"
	read e
	if [ $e == y ]
	then
		echo "Thank You & Byebye."
		break
	else
		echo "Returning to Menu"
		sleep 1.5
	fi
done
