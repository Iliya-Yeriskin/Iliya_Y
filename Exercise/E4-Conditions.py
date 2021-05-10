'''
Write a code that will show the menu:
Menu:
1.Insert Number and ** it by 3
2.Insert 4 IPs to a list and print it
3.Insert 4 Enteries to DNS_Dictionary and print it
4.Check if a string is Palindrom

if the user won't choose 1-4, you will tell him to insert 1-4 only!
'''
from time import sleep
choise=input(print("Hello \nMenu:\n1.Insert Number and ** it by 3\n2.Insert 4 IPs to a list and print it\n3.Insert 4 Enteries to DNS_Dictionary and print it\n4.Check if a string is Polindrom\nPlease choose a number from the menu: \n"))
if (choise=="1"):
    num1=int(input(("Please insert a number:" )))
    print("Calculating...\n--------------")
    sleep(2)
    print("Your number is: "+str(num1**3)+"\n--------------")
elif (choise=="2"):
    print("Please insert 4 IP addresses(after each IP press Enter to submit it): ")
    ip_list=[]
    ip_list.append(input("Enter New IP: "))
    ip_list.append(input("Enter New IP: "))
    ip_list.append(input("Enter New IP: "))
    ip_list.append(input("Enter New IP: "))
    print("----------------\nGenerating IP list\n----------------")
    sleep(2)
    print("This is the list of your IPs: "+str(ip_list))
elif (choise=="3"):
    print("Please insert 4 sites to your DNS_Dictionary\n")
    dns_dict={}
    dns_dict.update({input("Enter URL: "): input("Enter IP: ")})
    dns_dict.update({input("Enter URL: "): input("Enter IP: ")})
    dns_dict.update({input("Enter URL: "): input("Enter IP: ")})
    dns_dict.update({input("Enter URL: "): input("Enter IP: ")})
    print("-------------------\nGenerating DNS Dictionary\n-------------------")
    sleep(2)
    print("This is your DNS_Dictionary: "+str(dns_dict))
elif (choise=="4"):
    string = input(("Enter a string:\n"))
    print("Checking if its a palindrome..\n------------")
    sleep(2)
    if (string == string[::-1]):
        print("The string is a palindrome")
    else:
        print("Not a palindrome")
else:
    print("Enter numbers only!")





