"""Consider the mathematical expression (a+b)^2=(a^2+2ab+b^2). Write a Python
program that takes user input for values of a and b, then evaluates both sides of
the expression. Finally, compare the results and print whether the equation holds
true or false."""

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
LHS = (a + b) ** 2
RHS = a ** 2 + 2 * a * b + b ** 2

# Comparing both sides and printing the result
if LHS == RHS:
    print("The equation is true.")
else:
    print("The equation is not true.")

"""
O/P:
Enter the value of a: 1
Enter the value of b: 2
The equation is true.
"""
