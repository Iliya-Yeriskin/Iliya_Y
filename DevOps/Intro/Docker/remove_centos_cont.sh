#!/bin/bash


num=1
for i in `sudo docker ps -a | grep centos | awk '{print$1}'`
do
        sudo docker rm -f $i
        echo "Removed CentOS Container #$num"
        let num++
done