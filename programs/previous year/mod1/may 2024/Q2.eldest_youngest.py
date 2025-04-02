"""Write a python program to find out the eldest and youngest of three individuals ,
with their ages being input through the keyboard.(without using max, min functions)"""

a1=int(input("enter the age of individual 1: "))
a2=int(input("enter the age of individual 2: "))
a3=int(input("enter the age of individual 3: "))

if a1>a2 and a1>a3 :
    print(f"Individual 1 is eldest.")
elif a2>a1 and a2>a3:
    print(f"Individual 2 is eldest.")
else:
    print(f"Individual 3 is eldest.") 

if a1<a2 and a1<a3 :
    print(f"Individual 1 is youngest.")
elif a2<a1 and a2<a3:
    print(f"Individual 2 is youngest.")
else:
    print(f"Individual 3 is youngest.") 

"""
O/P:
enter the age of individual 1: 45
enter the age of individual 2: 65
enter the age of individual 3: 32
Individual 2 is eldest.
Individual 3 is youngest.

"""
