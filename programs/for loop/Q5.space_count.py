#count space character in a string

s=input("enter the string: ")
count=0
for i in s:
    if i==" ":
        count+=1
print("the no of space character is " ,count)

"""
O/P:
enter the string: Hello how are you
the no of space character is  3
"""