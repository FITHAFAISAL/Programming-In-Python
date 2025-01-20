#Question: Write a Python program to find distance between two points (x1,y1) and (x2,y2).

import math
x1=int(input("Enter the x1 Coordinates : "))
y1=int(input("Enter the y1 Coordinates : "))
x2=int(input("Enter the x2 Coordinates : "))
y2=int(input("Enter the y2 Coordinates : "))

dX = x2-x1
dY = y2-y1
distance = math.sqrt(dX**2 + dY**2)
print(f"Distance between ({x1},{y1}) and ({x2},{y2}): {distance}")

"""
O/P:
Enter the x1 Coordinates : 6
Enter the y1 Coordinates : 4
Enter the x2 Coordinates : 5
Enter the y2 Coordinates : 2
Distance between (6,4) and (5,2): 2.23606797749979
"""