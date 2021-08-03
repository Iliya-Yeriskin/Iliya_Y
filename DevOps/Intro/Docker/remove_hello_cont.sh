#!/bin/bash


num=1
for i in `sudo docker ps -a | grep helloworld | awk '{print$1}'`
do
        sudo docker rm -f $i
        echo "Removed adejonge/helloworld Container #$num"
        let num++
done