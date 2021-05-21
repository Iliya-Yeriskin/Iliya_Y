'''
check if the list is by Fibonacci law
'''

fibo = [1, 2, 3, 5, 9, 13, 21]
print("Please Enter a list of numbers: ")
counter = 7
fibo2 = []
while counter > 0:
    fibo2.append(int(input("Enter a number: ")))
    counter = counter-1
    print(fibo2)
boolean = "True"
for i in range(2, len(fibo2)):
    print(fibo2[i])
    print(fibo2[i-1])
    print(fibo2[i-2], "\n")
    if fibo2[i-2] + fibo2[i-1] == fibo2[i]:
        print(fibo2)
        continue
    else:
        boolean = "False"
        break
if boolean == "True":
    print("Its Fibonacci series")
else:
    print("Its not Fibonacci series")
