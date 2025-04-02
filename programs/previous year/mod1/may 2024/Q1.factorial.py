#Write a python program to print factorial of a given number.

n=int(input("enter the number: "))
fact=1
for i in range (1,n+1):
    fact*=i
print(f"factorial of {n}={fact}")

"""
O/P:
enter the number: 6
factorial of 6=720

"""