'''
Write a Python function that takes a positive integer and returns the sum
 of the cube of all the positive integers smaller than the specified number.
'''


num = int(input("Please enter a number between 1-10: "))


def cube(x):
    x = x-1
    tot = 0
    for i in range(0,x):
        tot = tot + (x * x * x)
        x = x-1
    return tot


print("Sum of all positive integers under your number: "+str(cube(num)))
