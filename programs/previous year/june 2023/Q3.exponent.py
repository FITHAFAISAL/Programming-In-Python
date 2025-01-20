#  Write a python program to find X^Y or pow(X,Y) without using standard function
x = float(input("Enter the base (X): "))
y = int(input("Enter the exponent (Y): "))
result = 1
is_negative_exponent = y < 0  
y = abs(y) 

for _ in range(y):
    result *= x
if is_negative_exponent:
    result = 1 / result

print(f"{x}^{y} = {result}")

"""
O/P:
Enter the base (X): 5
Enter the exponent (Y): -4
5.0^4 = 0.0016

"""
