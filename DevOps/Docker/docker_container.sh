#!/bin/bash

container() {
e="y"
while [ $e == "y" ]
do
    echo -e "Which Container would you like to Install?\n___________________________________________\n1.Jenkins\n2.CentOS\n3.Nginx\n4.DockerUI\n5.adejonge/helloworld"
    read choise5
    echo -e "How Many of Containers?"
    read multi
    if [ $choise5 == "1" ]
    then
            echo "You choose 1"
            count=1
            while [ $count -le $multi ]
            do
              echo "Please Enter port number:"
              read port
              for i in `sudo docker ps -a | grep ::: | awk '{print$1}'`
              do
                check="`sudo docker port $i | grep ::: | awk "NR==1" | cut -d ":" -f4`"
                echo $check >>ports11.txt
              done
              while grep $port ports11.txt
              do
                echo -e "**Sorry this port is used**\n___________________________\nEnter new port number: "
                read port
                continue
              done
              rm ports11.txt
              sudo docker run -d -p $port:8080 jenkins/jenkins
              echo "Container #$count Running"
              let count++
            done
    elif [ $choise5 == "2" ]
    then
            echo "You choose 2"
            count=1
            while [ $count -le $multi ]
            do
              sudo docker run -d centos
              echo "Container #$count Running"
              let count++
            done
    elif [ $choise5 == "3" ]
    then
            echo "You choose 3"
            count=1
            while [ $count -le $multi ]
            do
              echo "Please Enter port number:"
              read port
              for i in `sudo docker ps -a | grep ::: | awk '{print$1}'`
              do
                check="`sudo docker port $i | grep ::: | awk "NR==1" | cut -d ":" -f4`"
                echo $check >>ports11.txt
              done
              while grep $port ports11.txt
              do
                echo -e "**Sorry this port is used**\n___________________________\nEnter new port number: "
                read port
                continue
              done
              rm ports11.txt
              sudo docker run -d -p $port:80 nginx
              echo "Container #$count Running"
              let count++
            done
    elif [ $choise5 == "4" ]
    then
            echo "You choose 4"
            count=1
            while [ $count -le $multi ]
            do
              echo "Please Enter port number:"
              read port
              for i in `sudo docker ps -a | grep ::: | awk '{print$1}'`
              do
                check="`sudo docker port $i | grep ::: | awk "NR==1" | cut -d ":" -f4`"
                echo $check >>ports11.txt
              done
              while grep $port ports11.txt
              do
                echo -e "**Sorry this port is used**\n___________________________\nEnter new port number: "
                read port
                continue
              done
              rm ports11.txt
              sudo docker run -d -p $port:9000 -v /var/run/docker.sock:/docker.sock \ --name dockerui abh1nav/dockerui:latest -e="/docker.sock"
              echo "Container #$count Running"
              let count++
            done
    elif [ $choise5 == "5" ]
    then
            echo "You choose 5"
            count=1
            while [ $count -le $multi ]
            do
              echo "Please Enter port number:"
              read port
              for i in `sudo docker ps -a | grep ::: | awk '{print$1}'`
              do
                check="`sudo docker port $i | grep ::: | awk "NR==1" | cut -d ":" -f4`"
                echo $check >>ports11.txt
              done
              while grep $port ports11.txt
              do
                echo -e "**Sorry this port is used**\n___________________________\nEnter new port number: "
                read port
                continue
              done
              rm ports11.txt
              sudo docker run -d -p $port:8080 adejonge/helloworld
              echo "Container #$count Running"
              let count++
            done
    else
            echo "Please choose 1-5 ONLY!!!"
    fi
    echo "Do you want to Install another Container? (y/n)"
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