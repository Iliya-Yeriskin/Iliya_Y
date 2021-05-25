'''
Write a Python program to solve (x + y) * (x + y).
 Test Data : x = 4, y = 3
 Expected Output : (4 + 3) ^ 2) = 49
'''


def math(x, y):
    sum = int(x) + int(y)
    res = sum*sum
    print("("+x+" + "+y+")"+" ^ "+"2) ="+" "+str(res))


a = input("Please enter 1st number: ")
b = input("Please enter 2nd number: ")
math(a, b)

