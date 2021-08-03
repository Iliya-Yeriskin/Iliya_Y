#!/bin/bash

echo "Please enter port"
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
