'''
Write a Python program that accepts an integer (n) and computes the
 value of n+nn+nnn
 Sample value of n is 5
 Expected Result : 615
'''

num = int(input("Please enter a number: "))
sum = (int("%s" % (num)) + int("%s%s" % (num,num)) + int("%s%s%s" % (num,num,num)))
print(sum)
