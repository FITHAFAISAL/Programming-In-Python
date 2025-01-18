a=float(input("enter the first side: "))
b=float(input("enter the second side: "))
c=float(input("enter the third side: "))
if (a+b > c) and (a+c > b) and (b+c > a):
    print("These sides can form a valid triangle.")
else:
     print("These sides cannot form a valid triangle.")

"""
O/P:
enter the first side: 5
enter the second side: 6
enter the third side: 10
These sides can form a valid triangle.

"""