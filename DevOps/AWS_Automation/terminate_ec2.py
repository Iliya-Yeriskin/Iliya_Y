#!/bin/python3

import boto3

times = int(input("How many Instances you want to Terminate?\nEnter num: "))
ids = []
for i in range(times):
    instances=input("Enter the ID of the instance you want to terminate: ")
    ids.append(instances)
ec2 = boto3.resource('ec2')
ec2.instances.filter(InstanceIds=ids).terminate()