#print prime numbers btw 2 numbers

a=int(input("enter the starting number: "))
b=int(input("enter the ending number: "))
print(f"prime numbers between {a} and {b} are ")
for i in range (a,b+1):
    if i>1:
        is_prime =True
        for j in range (2,int(i**0.5)+1):
            if i %j ==0:
                is_prime =False
                break
        if is_prime:
            print(i,end=" ")

"""
O/P:
enter the starting number: 10
enter the ending number: 30
prime numbers between 10 and 30 are 
11 13 17 19 23 29
"""