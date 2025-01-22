#Write a Python program to count the number of occurances of a character in a given string without using count() method

s = input("Enter a string: ")
char = input("Enter the character to count: ")
count = 0
for i in s:
    if i== char:
        count += 1
print(f"the {char} occured {count} times in the {s}.")

"""
O/P:
Enter a string: program
Enter the character to count: r
the r occured 2 times in the program.

"""
