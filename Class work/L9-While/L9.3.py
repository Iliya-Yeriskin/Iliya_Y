from time import sleep
while True:
    choice = input(
        '\nHello \nMenu:\n1.Insert Number and ** it by 3\n2.Insert 4 IPs to a list and print it\n3.Insert 4 Entries to '
        'DNS_Dictionary and print it\n4.Check if a string is Palindrome\nPlease choose a number from the menu: ')
    if choice == "1":
        num1 = int(input("Please insert a number:"))
        print("Calculating...\n--------------")
        sleep(2)
        print("Your number is: " + str(num1 ** 3) + "\n--------------")
    elif choice == "2":
        print("Please insert 4 IP addresses(after each IP press Enter to submit it): ")
        ip_list = [input("Enter New IP: "), input("Enter New IP: "), input("Enter New IP: "), input("Enter New IP: ")]
        print("----------------\nGenerating IP list\n----------------")
        sleep(2)
        print("This is the list of your IPs: " + str(ip_list))
    elif choice == "3":
        print("Please insert 4 sites to your DNS_Dictionary\n")
        dns_dict = {}
        dns_dict.update({input("Enter URL: "): input("Enter IP: ")})
        dns_dict.update({input("Enter URL: "): input("Enter IP: ")})
        dns_dict.update({input("Enter URL: "): input("Enter IP: ")})
        dns_dict.update({input("Enter URL: "): input("Enter IP: ")})
        print("-------------------\nGenerating DNS Dictionary\n-------------------")
        sleep(2)
        print("This is your DNS_Dictionary: " + str(dns_dict))
    elif choice == "4":
        string = input("Enter a string:\n")
        print("Checking if its a palindrome..\n------------")
        sleep(2)
        if string == string[::-1]:
            print("The string is a palindrome")
        else:
            print("Not a palindrome")
    else:
        print("Enter 1-4 only!")
    exit = input("Do you want to exit?(y/n)")
    if exit == "y" or exit == "yes":
        break
    elif exit == "n" or exit == "no":
        continue
    sleep(1)
print("\nThank you Bye Bye")
