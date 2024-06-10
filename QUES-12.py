#  Write a python program that calculates the sum of the digits of a given number.

def sum_of_digits(num):
    string = str(num)
    total = 0
    for char in string: 
        total += int(char)
    return total

number = int(input("enter a number: "))

Digit_sum = sum_of_digits(number)

print(f"The sum of the digits of the given number{number} is {Digit_sum}. ")