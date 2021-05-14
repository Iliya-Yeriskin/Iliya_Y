'''
10. Write a Python program to create a dictionary from a string. Note: Track the count of the letters from the string.
Sample string : 'Net4U'
Expected output: {'N': 1, 'e': 1, 't': 2, '4': 1, 'U': 1}
'''

word=input("Please enter a word: ")
dict={i:word.count(i) for i in word}
print(dict)

