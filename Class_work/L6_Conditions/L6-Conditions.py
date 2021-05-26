#Conditions
name=input("Enter a name: ")
if(name=="iliya"):#checking if the name that was inputed is correct
    print("Hello Iliya\n")
    age = int(input("Enter a age: "))
    if (age == 28):#check if age is correct
        print("Great, you may enter\n")
    else:
        print("Sorry, you are too young\n")
else:
    print("Sorry, you're not in the list\n")


