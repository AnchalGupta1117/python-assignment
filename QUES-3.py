#Write a python program that calculates the factorial of a given number.

number = int(input("enter a number: "))
def factorial(num):
    if (num == 0 or num == 1): 
        return 1
    else: 
        return   num*factorial(num-1)
result = factorial(number)
print(f"the factorial of {number} is {result},")