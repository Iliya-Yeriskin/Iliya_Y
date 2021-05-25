'''
Write a Python program to display your details like name, age, address in
 three different lines.
'''


from time import sleep


def name():
    while True:
        name = input("Enter your Name: ")
        age = input("Enter your Age: ")
        color = input("Enter your Address: ")
        print("Saving Data.........")
        sleep(2)
        correct = input("Your details was saved.\n----------------------------\nYour Details:"+"\nName: " +
                        str(name)+"\nAge: "+str(age)+"\nAddress: "+color+"\n----------------------------\nPlease "
                                                                       "confirm the details correct y/n?: ")
        if correct == "y":
            break
        else:
            continue


name()
print("Thank you, See you soon.")
