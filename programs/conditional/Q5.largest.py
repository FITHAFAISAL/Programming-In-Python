# print the largest number of 3 numbers

a=int(input("enter the no 1: "))
b=int(input("enter the no 2: "))
c=int(input("enter the no 3: "))

if a>b and a>c :
    print(f"{a} is the largest number.")
elif b>a and b>c :
    print(f"{b} is the largest number.")
else:
    print(f"{c} is the largest number.")

"""
O/P:
enter the no 1: 45
enter the no 2: 89
enter the no 3: 66
89 is the largest number.

"""