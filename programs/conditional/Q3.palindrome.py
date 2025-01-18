# check whether the string is palindrome

s=input("enter the string: ")
if s==s[::-1]:
    print("the string is palindrome.")
else:
    print("the string is not palindrome.")

"""
O/P:
enter the string: malayalam
the string is palindrome.

"""