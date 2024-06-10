#  Write a python program that counts the occurrences of a specific element in a list.

def count_occurences(list,element):
    count = list.count(element)
    print("occurrences of a specific element in the list is: ", count)

given_list = list(input("enter a list: "))
given_element = input("enter the specific element whose occurence you want to count: ")

count_occurences(given_list,given_element)