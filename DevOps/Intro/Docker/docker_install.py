#!/bin/bash

install_image() {
e="y"
while [ $e == "y" ]
do
    echo -e "Which Image would you like to install?\n___________________________________________\n1.Jenkins\n2.CentOS\n3.Nginx\n4.DockerUI\n5.adejonge/helloworld"
    read choise2
    if [ $choise2 == "1" ]
    then
            echo "You choose 1"
            sudo docker pull jenkins/jenkins
    elif [ $choise2 == "2" ]
    then
            echo "You choose 2"
            sudo docker pull centos
    elif [ $choise2 == "3" ]
    then
            echo "You choose 3"
            sudo docker pull  nginx
    elif [ $choise2 == "4" ]
    then
            echo "You choose 4"
            sudo docker pull abh1nav/dockerui
    elif [ $choise2 == "5" ]
    then
            echo "You Choose 5"
            sudo docker pull adejonge/helloworld
    else
            echo "Please choose 1-5 ONLY!!!"
    fi
    echo "Do you want to Install another Image? (y/n)"
    read e
    if [ $e == n ]
    then
            echo "Thank You & Byebye."
            break
    else
            echo "Returning to Menu"
            sleep 1.5
    fi
done
}