#!/bin/bash

update_image() {
e="y"
while [ $e == "y" ]
do
    echo -e "Which Image would you like to Update?\n___________________________________________\n1.Jenkins\n2.CentOS\n3.Nginx\n4.DockerUI\n5.adejonge/helloworld"
    read choise4
    if [ $choise4 == "1" ]
    then
            echo "You choose 1"
            sudo docker pull jenkins/jenkins:latest
            sleep 1
            echo "Done updateing jenkins"
    elif [ $choise4 == "2" ]
    then
            echo "You choose 2"
            sudo docker pull centos:latest
            sleep 1
            echo "Done updating CentOS"
    elif [ $choise4 == "3" ]
    then
            echo "You choose 3"
            sudo docker pull nginx
            sleep 1
            echo "Done updating Nginx"
    elif [ $choise4 == "4" ]
    then
            echo "You choose 4"
            sudo docker pull abh1nav/dockerui:latest
            sleep 1
            echo "Done updating DockerUI"
    elif [ $choise4 == "5" ]
    then
            echo "You Choose 5"
            sudo docker pull adejonge/helloworld:latest
            sleep 1
            echo "Done updating adejonge/helloworld"
    else
            echo "Please choose 1-5 ONLY!!!"
    fi
    echo "Do you want to Update another Image? (y/n)"
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