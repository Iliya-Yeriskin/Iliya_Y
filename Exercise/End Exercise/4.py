'''
Write a Python program to calculate number of days between two dates.
 Sample dates : (2014, 7, 2), (2014, 7, 11)
 Expected output : 9 days
'''
import datetime
d0 = datetime.date(2014, 7, 2)
d1 = datetime.date(2014, 7, 11)

delta = d1 - d0
print(str(delta.days)+" days")


