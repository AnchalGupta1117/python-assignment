# Write a python program that converts a given string to uppercase.


def to_uppercase(str):
    return str.upper()

string = input("enter a string that you want to convert into uppercase: ")
newStr = to_uppercase(string)
print(newStr)