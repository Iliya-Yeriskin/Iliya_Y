'''
1)Create a list with 4 details about you: name, age, email, phone and print them on screen
2)Create another list with 2 IPs, then add more 3 IPs, pop the 3rd IP and print how many IPs do we have and print them.
'''
#1
my_list=["Iliya","28","iliya@gmail.com","052-123-4567"]
print("My name is: "+my_list[0]+"\nMy Age is: "+my_list[1]+"\nMy Email is: "+my_list[2]+"\nMy Phone is: "+my_list[3])

#2
ip_list=["192.168.1.1","1.2.3.4"]
print("IP List: " + str(ip_list))
#adding 3 IP to ip_list
ip_list.append("1.1.1.1")
ip_list.append("2.2.2.2")
ip_list.append("3.3.3.3")
print(ip_list)
#deleting the 3rd ip
ip_list.pop(2)
#printing the length of the list
print("IP List length is: "+str(len(ip_list)))
#printing all the IP in the list
print("Our IP List includes:\n1st IP: "+ip_list[0]+"\n2nd IP: "+ip_list[1]+"\n3rd IP: "+ip_list[2]+"\n4th IP: "+ip_list[3])

