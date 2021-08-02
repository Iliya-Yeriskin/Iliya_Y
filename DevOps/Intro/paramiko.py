#!/bin/python3

import paramiko

nbytes = 4096
hostname = 'ubuntu2'
port = 22
username = 'iliya'
password = 'rootroot'
command = '''
mkdir /home/iliya/Desktop/paramiko/1st_try
cd /home/iliya/Desktop/paramiko/1st_try
touch par.txt
echo "its working" > par.txt'''

client = paramiko.Transport((hostname, port))
client.connect(username=username, password=password)

stdout_data = []
stderr_data = []
session = client.open_channel(kind='session')
session.exec_command(command)

session.close()
client.close()