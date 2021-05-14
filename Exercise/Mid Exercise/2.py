'''
2. Write a Python program to display the current date and time. Sample Output :
Current date and time :
14:34:14 2014-07-05
'''
import datetime
now = datetime.datetime.now()
print ("Current date and time: \n"+now.strftime("%Y-%m-%d %H:%M:%S"))