'''
Write a Python program to sum of two given integers. However, if the sum
 is between 15 to 20 it will return 20.
'''


def summery(x,y):
    sum = x + y
    if sum in range(15, 20):
        sum = 20
    return sum


print(summery(3,7))
print(summery(11,7))
print(summery(12,14))
print(summery(11,4))
print(summery(8,1))
print(summery(10,10))
print(summery(10,4))