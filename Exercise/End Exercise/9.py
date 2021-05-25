'''
Write a Python program to convert height (in feet and inches) to
 centimeters
'''


h = float(input("Please enter your height(foot.inch): "))
cm = float(h*30.48)
print("Your height in Centimeters is: "+str("%.2f" % cm)+"cm")
