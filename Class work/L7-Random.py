#Random

from random import randint
from time import sleep
print("Getting random numbers...\n")
sleep(2)
num1=randint(1,10)
num2=randint(1,10)
print("1st Number: " +str(num1) + "\n2nd Number: "+str(num2))
if (num1==num2):
    print("You Won 100$\n")
else:
    print("You Won 0$\n")

print("Bye Bye\n")


