# Write a program in python that converts a given string to title case (first letter of each word capitalized).

def title_case(str):
    new_str = str.title()
    print (new_str)

string = input("enter a string: ")
title_case(string)