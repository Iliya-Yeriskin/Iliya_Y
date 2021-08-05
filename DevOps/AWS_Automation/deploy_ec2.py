#!/bin/python3

from time import sleep
import boto3

ec2 = boto3.resource('ec2')
# create a new EC2 instance
image = input("Choose Image: ")
num_of_ins = int(input("Choose number of instances:"))
instances = ec2.create_instances(
        ImageId=image,
        MinCount=1,
        MaxCount=num_of_ins,
        InstanceType='t2.micro',
        KeyName='aws_automation',
)
sleep(1)
print("The Instances Deployed")