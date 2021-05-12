#LOOPS
from time import sleep
print("Now we will get all the details about your class: \n")
for i in range(1,3):
    name=input("Enter your name: ")
    age=input("Enter your age: ")
    phone=input("Enter your phone: ")
    print("---------------------\nPrinting student number: #"+str(i)+" Details...")
    sleep(2)
    print("---------------------\nFull name: "+name+"\nAge: "+age+"\nPhone: "+phone+"\n-------------------")


print("\nThank you we submmited all the details.")

