'''
Menu:
1.Dogs Details
2.Friends list
3.N Azzeret
'''

from time import sleep


def dogs():
    while True:
        name = input("Enter your dogs name: ")
        age = input("Enter your dogs age: ")
        color = input("Enter your dogs color: ")
        print("Saving Data.........")
        sleep(2)
        correct = input("Your dog's details was saved.\n----------------------------\nDogs Details:"+"\nName: " +
                        str(name)+"\nAge: "+str(age)+"\nColor: "+color+"\n----------------------------\nPlease "
                                                                       "confirm the details correct y/n?: ")
        if correct == "y":
            break
        else:
            continue


def friends():
    f_list = []
    counter = int(input("How many friends do you want to invite?: "))
    while counter > 0:
        f_list.append(input("Enter Name: "))
        counter = counter-1
    print("-------------------\nGenerating list....")
    sleep(1.5)
    print("\nThat's your friend list that are invited to the event:\n"+str(f_list))


def azzeret():
    print("This function will count the factorial number of your chosen number")
    num = int(input("Please Enter a number between 1-10: "))
    n1 = 1
    for i in range(1, num+1):
        n1 = i * n1
    print("The Factorial number of: "+str(num)+" is: "+str(n1))


def menu():
    while True:
        print("\nHello\nMenu:\n1.Dogs Details\n2.Friends list\n3.Factorial number(Azzeret)")
        choise = int(input("\nPlease enter your choise: "))
        if choise == 1:
            dogs()
        elif choise == 2:
            friends()
        elif choise == 3:
            azzeret()
        else:
            print("Please enter ONLY 1-3!!")
        exit = input("\nDo you want to exit y/n? ")
        if exit == "y":
            break
        else:
            continue


menu()
print("\n------------------------\nThank you and Byebye...")
