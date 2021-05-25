'''
Write a Python program to convert a byte string to a list of integers.
'''


def byte(x):
    list = []
    for i in x:
        list.append(i)
    print(list)


byte(b'iliya')
