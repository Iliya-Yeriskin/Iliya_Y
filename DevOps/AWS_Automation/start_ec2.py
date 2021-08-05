#!/bin/python3

import boto3

ec2 = boto3.resource('ec2')
times = int(input("How many Instances you want to Start?\nEnter num: "))
ids = []
for i in range(times):
    instances = input("Enter the ID of the instance you want to Start: ")
    ids.append(instances)
ec2.instances.filter(InstanceIds=ids).start()