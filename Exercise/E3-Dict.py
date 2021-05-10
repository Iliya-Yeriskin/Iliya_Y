'''
1.Create a dictionary with 5 names & money
then sum the money of the 1st & 5th names and print it to screen.
2.Add a new name with the sum of the money you calculated before,
print the number of entries and check if "iliya" is inside
'''
name_dict={"iliya":40000,"idan":50000,"ben":20000,"yosi":10000,"david":60000}
print(name_dict)
#1st & 5th name money sum
sum=(name_dict["iliya"]+name_dict["david"])
print("The sum of 1st & 5th money count: "+str(sum)+"₪")
name_dict.update({"haim":sum})
print(name_dict)
print("Number of Entries: " +str(len(name_dict)))
print("iliya" in name_dict)