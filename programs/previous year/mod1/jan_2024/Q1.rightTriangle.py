"""Write a program that accepts the lengths of three sides of a triangle as inputs and
outputs whether or not the triangle is a right triangle."""

base=int(input("enter the base: "))
height=int(input("enter the height: "))
hypotenus=int(input("enter the hypotenus: "))

if (base**2)+(height**2)==(hypotenus**2):
    print("the triangle is a right angled triangle.")
else:
        print("the triangle is not a right angled triangle.")


"""
O/P:
enter the base: 3
enter the height: 4
enter the hypotenus: 5
the triangle is a right angled triangle.

"""