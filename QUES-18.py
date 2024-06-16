# Write a python program that checks if two strings are anagrams of each other.

str1 = input("enter string 1 : ")
str2 = input("enter string 2 : ")
def check_anagrams(str1,str2):
    new_str1 = sorted(str1)
    new_str2 = sorted(str2)
    return  new_str1 == new_str2
        
    

if check_anagrams(str1,str2):
    print("These two strings are anagrams of each other.")

else:
    print("These two strings are not anagrams of each other.")

