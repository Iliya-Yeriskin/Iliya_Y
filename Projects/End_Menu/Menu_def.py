from time import sleep
from Projects.End_Menu.list_of_ips_urls import list
from Projects.End_Menu.list_of_ips_urls import my_dict


def main_menu():
    while True:
        choise = input("\nMain Menu:\n---------------\nPlease choose your system:\n1.IP System\n2.DNS System?\n"
                       "Please enter your choise: ")
        if choise == "1":
            ip_system()
        elif choise == "2":
            dns_system()
        else:
            print("\n*** Enter ONLY 1-2!! ***")
            sleep(1)
            continue
        exit = input("Do you want to exit from the Main Menu? (y/n): ")
        if exit == "n":
            sleep(1)
            continue
        else:
            sleep(1)
            print("-------------------\nThank you Byebye.....\n-------------------")
            break


def ip_system():
    while True:
        choise = input("\nIP System Menu:\n---------------\n1.Search for IP address from list\n"
                       "2.add IP address to a list\n"
                       "3.Delete IP address from a list\n4.Print all the IPs to the screen\nPlease enter your choise: ")
        if choise == "1":
            search_ip()
        elif choise == "2":
            add_ip()
        elif choise == "3":
            delete_ip()
        elif choise == "4":
            print_ips()
        else:
            print("\n*** Enter ONLY 1-4!! ***")
            sleep(1)
            continue
        exit = input("Do you want to exit from IP System? (y/n): ")
        if exit == "n":
            continue
        else:
            sleep(0.5)
            print("-------------------\nThank you Byebye.....\n-------------------")
            break


def dns_system():
    while True:
        choise = input("\nDNS System Menu:\n--------------\n1.Search for URL from a dictionary\n"
                       "2.add URL + IP address to a dictionary\n"
                       "3.Delete URL from dictionary\n4.Update the IP address of a specific URL\n"
                       "5.Print all the URL:IP to the screen\nPlease enter your choise: ")
        if choise == "1":
            search_dns()
        elif choise == "2":
            add_dns()
        elif choise == "3":
            delete_dns()
        elif choise == "4":
            update_dns()
        elif choise == "5":
            print_dns()
        else:
            print("\n*** Enter ONLY 1-5!! ***")
            sleep(1)
            continue
        exit = input("Do you want to exit from DNS System? (y/n): ")
        if exit == "n":
            continue
        else:
            sleep(1)
            print("-------------------\nThank you Byebye.....\n-------------------")
            break


def search_ip():
    ip = input("Enter IP to search: ")
    if ip in list:
        print("Yes the IP: " + str(ip) + " is in the list")
    else:
        print("The IP: " + str(ip) + " is not in the list")
        q1 = input("Do you want to add the ip to the list (y/n)?: ")
        if q1 == "y":
            list.append(ip)
            print("The IP added to the list\nPrinting new list....")
            sleep(1)
            print("New list: " + str(list))


def add_ip():
    ipadd = input("Please enter IP to the List: ")
    list.append(ipadd)
    print("The IP added to the list\nPrinting new list....")
    sleep(1)
    print("New list: " + str(list))


def delete_ip():
    print("What IP do you want to Delete from the list?")
    counter = 1
    for i in list:
        print(str(counter) + ") " + i)
        counter = counter + 1
    delete = int(input("Please enter the IP location number: ")) - 1
    list.pop(delete)
    sleep(1)
    print("Your selected IP was deleted.\nNew IP list: " + str(list))


def print_ips():
    print("The IPs in the list:")
    counter = 1
    for i in list:
        print(str(counter) + ") " + i)
        counter = counter + 1


def search_dns():
    url = input("Enter URL to search: ")
    if url in my_dict:
        print("Yes the URL: " + str(url) + " is in the dictionary")
    else:
        print("The URL: " + str(url) + " is not in the dictionary")
        q1 = input("Do you want to add the URL to the dictionary (y/n)?: ")
        if q1 == "y":
            ip = input("Please enter the URL IP address: ")
            my_dict.update({url: ip})
            print("The URL added to the dictionary\nPrinting new dictionary....")
            sleep(1)
            print("New Dictionary: " + str(my_dict))


def add_dns():
    url1 = input("Please enter URL to the dictionary: ")
    ip1 = input("Please enter the URL's IP address: ")
    my_dict.update({url1: ip1})
    print("The URL added to the dictionary\nPrinting new dictionary....")
    sleep(1)
    print("New Dictionary: " + str(my_dict))


def delete_dns():
    print("What URL do you want to Delete from the dictionary?")
    counter = 1
    for i in my_dict:
        print(str(counter) + ") " + i)
        counter = counter + 1
    delete = input("Please enter the URL: ")
    my_dict.pop(delete)
    sleep(1)
    print("Your selected URL was deleted.\nNew URL dictionary: " + str(my_dict))


def update_dns():
    print("For which URL you want to update the IP address: ")
    counter = 1
    for i in my_dict:
        print(str(counter) + ") " + i + " : " + my_dict[i])
        counter = counter + 1
    url2 = input("Please enter the URL: ")
    update = input("Please enter new IP for this URL: ")
    my_dict[url2] = update
    print("New URL dictionary: " + str(my_dict))


def print_dns():
    print("All the URL's in the dictionary: ")
    counter = 1
    for i in my_dict:
        print(str(counter) + ") " + i + " : " + my_dict[i])
        counter = counter + 1


