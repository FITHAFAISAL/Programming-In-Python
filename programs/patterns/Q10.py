n=int(input("enter the number: "))
for i in range (1,n+1):
    print ("* "*i)
for j in range(n-1,0,-1):
    print("* "*j)

"""
O/P:
enter the number: 5
* 
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

"""