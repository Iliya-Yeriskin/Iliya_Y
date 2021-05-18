'''
Write a Python program to count repeated characters in a string.
  Sample string: 'thequickbrownfoxjumpsoverthelazydog'
  Expected output:
  o4
  e3
  u2
  h2
  r2
  t2
'''

st="thequickbrownfoxjumpsoverthelazydog"
dict={}
for i in "abcdefghijklmnopqrstuvwxyz":
    c=st.count(i)
    if c>1:
        print(i+str(c))