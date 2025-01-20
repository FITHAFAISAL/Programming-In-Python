#print digits of a number and reverse

n = int(input("Enter the number: "))
digits = []
rev = 0
while n > 0:
    digits.append(n % 10)  
    rev = rev * 10 + (n % 10)  
    n = n // 10  
print("Digits of the number:", digits)
print("Reversed number:", rev)

"""
O/P:
Enter the number: 123
Digits of the number: [3, 2, 1]
Reversed number: 321

"""