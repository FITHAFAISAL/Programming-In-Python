"""Write a python program to generate the following type of pattern for the given Nrows where N <= 26.
A
A B
A B C D
A B C D E"""

N = int(input("Enter the number of rows : "))


if N <=26:
    for i in range(1, N + 1):
        for j in range(i):
            print(chr(65 + j), end=" ")
        print()  

"""
O/P:
Enter the number of rows : 5
A 
A B
A B C
A B C D
A B C D E

"""