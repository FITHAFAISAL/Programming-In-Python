#Write a Python program to display the sum of odd numbers between a programmer specified upper and lower limit.

lower=int(input("Enter the lower limit: "))
upper=int(input("Enter the upper limit: "))
sum=0
for i in range (lower,upper+1):
    if i % 2 !=0:
        sum+=i
print(f"sum of odd numbers between {lower} and {upper} is {sum}")

"""
O/P:
Enter the lower limit: 3
Enter the upper limit: 9
sum of odd numbers between 3 and 9 is 24

"""