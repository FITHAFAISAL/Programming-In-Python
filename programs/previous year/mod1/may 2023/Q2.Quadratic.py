#Write a Python program to find the roots of a quadratic equation, ax^2 + bx + c = 0 . Consider the cases of both real and imaginary roots.

import cmath  
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

if a == 0:
    print("The value of 'a' cannot be zero for a quadratic equation.")
else:
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    print(f"The roots of the equation are: {root1} and {root2}")
    if discriminant > 0:
        print("The equation has two distinct real roots.")
    elif discriminant == 0:
        print("The equation has two equal real roots.")
    else:
        print("The equation has two complex roots.")
"""
O/P:
Enter the coefficient a: 1
Enter the coefficient b: -3
Enter the coefficient c: 2
The roots of the equation are: (2+0j) and (1+0j)
The equation has two distinct real roots.

"""