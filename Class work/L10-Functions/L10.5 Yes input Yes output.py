def calculating(x,y):
    print("Your 1st number: " + str(x) +
          "\nYour 2nd number: " + str(y))
    sum = x*y
    print("Your new number is: " + str(sum))
    return sum


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
iliya = calculating(a,b) + 5
print("Post function number: " + str(iliya))

