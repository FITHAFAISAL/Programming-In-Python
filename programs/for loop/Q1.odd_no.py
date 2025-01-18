#print odd number between two limits

a = int(input("enter the lower limit:"))
b = int (input("enter the upper limit: "))
for i in range (a,b+1):
    if(i%2!=0):
        print(i,end=" ")

"""
O/P:
enter the lower limit:3
enter the upper limit: 12
3 5 7 9 11 
"""