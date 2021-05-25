'''
Write a Python program to calculate the sum of three given numbers, if
 the values are equal then return three times of their sum.
'''


def summery(a, b, c):
    sum = a + b + c
    if a == b == c:
        sum = sum * 3
    return sum


print(summery(1, 2, 3))
print(summery(2, 2, 2))
