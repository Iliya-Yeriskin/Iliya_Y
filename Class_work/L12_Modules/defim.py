from random import randint


def calculating(a,b):
    c = int(input("Enter a number: "))
    sum = a*b*c
    print("The sum is: "+str(sum))


def dogs_age(a):
    b = a*7
    print("Real dogs age: " + str(b))
    return b


def menu():
    choise = input("Menu\n1.Printing 1-100\n2.Random 2 cubes")
    if choise == "1":
        for i in range(1,101):
            print(i)
    elif choise == "2":
        print("Cube 1: " + str(randint(1,6)))
        print("Cube 2: " + str(randint(1,6)))
    else:
        print("Enter 1-2 ONLY!!")


