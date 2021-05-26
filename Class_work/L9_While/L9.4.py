while True:
    name = input("Enter a name: ")
    if name == "iliya":
        print("Hello Iliya")
        break
    elif name == "dan":
        continue
    else:
        print("Where is Iliya?")
    number = int(input("Enter a number: "))
    print(number*4)
print("Bye Bye...")
