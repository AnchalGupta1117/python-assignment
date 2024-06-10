# Write a python program that checks if a substring is present in a given string.

str = input("enter a string: ")
subStr = input("enter the substring that you want to search for: ")
def check(str, subStr):
    if subStr in str:
        return True
    else:
        return False
if check(str, subStr):
    print("Substring is present.")
else:
    print("Substring is not present.")