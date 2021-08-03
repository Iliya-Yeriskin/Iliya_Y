#!/bin/bash

remove_image() {
e="y"
while [ $e == "y" ]
do
    echo -e "Which Image would you like to Remove?\n___________________________________________\n1.Jenkins\n2.CentOS\n3.Nginx\n4.DockerUI\n5.adejonge/helloworld"
    read choise3
    if [ $choise3 == "1" ]
    then
            echo "You choose 1"
            sudo docker rmi -f jenkins/jenkins >/dev/null
            sleep 1
            echo "Done removing jenkins"
    elif [ $choise3 == "2" ]
    then
            echo "You choose 2"
            sudo docker rmi -f centos >/dev/null
            sleep 1
            echo "Done removing CentOS"
    elif [ $choise3 == "3" ]
    then
            echo "You choose 3"
            sudo docker rmi -f  nginx >/dev/null
            sleep 1
            echo "Done removing Nginx"
    elif [ $choise3 == "4" ]
    then
            echo "You choose 4"
            sudo docker rmi -f abh1nav/dockerui >/dev/null
            sleep 1
            echo "Done removing DockerUI"
    elif [ $choise3 == "5" ]
    then
            echo "You Choose 5"
            sudo docker rmi -f adejonge/helloworld >/dev/null
            sleep 1
            echo "Done removing adejonge/helloworld"
    else
            echo "Please choose 1-5 ONLY!!!"
    fi
    echo "Do you want to Remove another Image? (y/n)"
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