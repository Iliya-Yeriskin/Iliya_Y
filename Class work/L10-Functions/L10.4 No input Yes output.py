def calculating():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    sum = num1 * num2
    print("Your new number is: " + str(sum))
    return sum


a = calculating() + 5
print("Post function number: " + str(a))
