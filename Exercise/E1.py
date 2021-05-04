'''
The number is in *num* give me the output of all the digits by thousand,hundred,ten,one like:
Alafim=4
Meot=5
Asarot=6
Ahadot=7
'''

num=int(input("Enter a number with 4 digits: "))
Alafim=num//1000
Meot=num%1000//100
Asarot=num%100//10
Ahadot=num%10//1
print("Alafim= " +str(Alafim) + "\nMeot= " +str(Meot) + "\nAsarot= " + str(Asarot) + "\nAhadot= " + str(Ahadot))