#check whether the year is leapyear

year = int(input("Enter the Year: "))
if year % 4 == 0:
    if year % 100 == 0 :
        if year % 400 == 0:
            print("The year is a Leap Year")
        else:
            print("The year is not a Leap Year")
    else:
        print("The year is  a Leap year")
else:
    print("The year is not a Leap year")

"""
O/P:
Enter the Year: 2024
The year is  a Leap year

"""