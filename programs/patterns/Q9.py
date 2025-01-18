n=int(input("enter the no: "))
for i in range (n,0,-1):
    for k in range (i,n):
        print(" ",end=" ")
    for j in range (1,i+1):
        print("*",end=" ")
    print(" ")

"""
O/P:
enter the no: 5
* * * * *  
  * * * *
    * * *
      * *
        *

"""