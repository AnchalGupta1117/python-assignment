#Write a python program that checks whether a given number is even or odd.

num = int(input("enter a number: "))
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
result = check_even_odd(num)
print(f"The number {num} is {result}.")