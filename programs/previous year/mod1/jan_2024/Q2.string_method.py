"""Assume that the variable data refers to the string "python rules!". use a string method to perform the following tasks
a)obtain a list of the words in the string
b)convert the string to uppercase
c)locate the position of the string "rule" """

s="python rules!"
#a)
s1=s.split()
print(s1)
print()

#b)
print(s.upper())
print()

#c)
print(s.find("rule"))