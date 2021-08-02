#!/bin/bash


num=1
for i in `sudo docker ps -a | grep nginx | awk '{print$1}'`
do
        sudo docker rm -f $i
        echo "Removed Nginx Container #$num"
        let num++
done