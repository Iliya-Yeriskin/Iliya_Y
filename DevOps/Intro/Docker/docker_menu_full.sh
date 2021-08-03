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


