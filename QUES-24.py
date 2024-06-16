# Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.

def sum_operator(num1,num2,operator):
    final = num1 + num2
    return final
def sub_operator(num1,num2,operator):
    final = num1 - num2
    return final
def mul_operator(num1,num2,operator):
    final = num1 * num2
    return final
def div_operator(num1,num2,operator):
    final = num1 / num2
    return final

def calculator():
    number1 = int(input("enter number 1: "))
    number2 = int(input("enter number 2: "))
    opr = input("enter the operator(+,-,*,/): ")
    if (opr == "+"):
        print(sum_operator(number1,number2,opr))
    elif (opr == "-"):
        print(sub_operator(number1,number2,opr))
    elif (opr == "*"):
        print(mul_operator(number1,number2,opr))
    elif (opr == "/"):
        print(div_operator(number1,number2,opr))

calculator()
