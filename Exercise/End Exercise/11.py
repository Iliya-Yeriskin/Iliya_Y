'''
Write a Python function that takes a positive integer and returns the sum
 of the cube of all the positive integers smaller than the specified number.
'''


num = int(input("Please enter a number between 1-10: "))


def cube(x):
    sum = 0
    for i in range(1,x):
        sum = sum + (i * i * i)
    return sum


print("Cube sum of all positive integers under your number: "+str(cube(num)))
