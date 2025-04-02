"""Write a Python program to check whether a number is Armstrong number or not.
 An Armstrong number is an n-digit number that is equal to the sum of the nth powers of its digits."""

n = int(input("Enter the Number: "))
temp=n
pow= 0
while temp > 0:
    pow += 1
    temp = temp//10
temp = n
result = 0

while temp > 0:
    digit = temp%10
    result += digit**pow
    temp = temp//10

if result== n:
    print(f"{n} is an amstrong number")
else:
    print(f"{n} is not an amstrong number")

"""
O/P:
Enter the Number: 153
153 is an amstrong number

"""