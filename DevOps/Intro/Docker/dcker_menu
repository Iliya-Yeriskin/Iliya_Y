#!/bin/bash

e="n"
while [ $e == "n" ]
do
        echo -e "Hello\n_________\nPlease choose an option:\n1.Install Images\n2.Remove Images\n3.Update Image\n4.Install Container(s)\n5.Show Installed Images\n6.Show Running Containers"
        read choise
        if [ $choise == "1" ]
        then
                echo "You choose 1"
                install_image
        elif [ $choise == "2" ]
        then
                echo "You choose 2"
                remove_image
        elif [ $choise == "3" ]
        then
                echo "You choose 3"
                update_image
        elif [ $choise == "4" ]
        then
                echo "You choose 4"
                container
        elif [ $choise == "5" ]
        then
                echo "You choose 5"
                sudo docker images
        elif [ $choise == "6" ]
        then
                echo "Youc hoose 6"
                sudo docker ps
        else
                echo "Please choose 1-6 ONLY!!!"
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