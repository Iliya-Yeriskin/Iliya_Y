#Function
from time import sleep
################
def Market():
    print("Hello\n---------------------\nToday in the Market:\nTomato = 3₪\nCucumber = 2₪\nCoca-Cola = 5₪\nChicken = 20₪")
    tomato = int(input("Enter How many Tomatos would you like? "))
    cucumber = int(input("Enter How many Cucumbers would you like? "))
    cola = int(input("Enter How many Coca-Colas would you like? "))
    chicken = int(input("Enter How many Chickens would you like? "))
    print("\n------------------\nCalculating.....\n------------------")
    sleep(2)
    print("\nSummery of your order:\n----------------------\nTomatos: " + str(tomato) + "\nCucumbers: " + str(cucumber) +
          "\nCoca-Cola: " + str(cola) + "\nChickens: " + str(chicken) + "\n----------------------")
    sleep(2)
    summary = (tomato*3)+(cucumber*2)+(cola*5)+(chicken*20)

    print("Your Bill is -------------------- " + str(summary) + "₪")
    print("\nYour Bill including TAX is ------ " + str("%.0f" % (summary*1.17)) + "₪\n----------------------")

##############
##### Main Code #####
for i in range(10):
    Market()