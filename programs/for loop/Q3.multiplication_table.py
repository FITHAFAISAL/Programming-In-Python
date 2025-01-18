#print multiplication table of a user input number

n=int(input("enter the number: "))
l=int(input("enter the limit:"))
for i in range (1,l+1):
    print(f"{n} * {i} = {n*i}")

"""
O/P:
enter the number: 5
enter the limit:10
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50

"""