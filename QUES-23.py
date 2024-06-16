# Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.

def temperature():
    temperature = input("Enter the temperature: ")
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter your choice (1 or 2): ")

    if (choice == "1"):
        celsius_to_Fahrenheit(temperature)
    else:
        Fahrenheit_to_Celsius(temperature)

def celsius_to_Fahrenheit(temp):
    celsius = int(temp)
    fahrenheit_temp =float( celsius*9/5 + 32 )
    print(" ",temp,"C =  ",fahrenheit_temp,"F" ) 

def Fahrenheit_to_Celsius (temp):
    Fahrenheit = int(temp)
    Celsius_temp = float((Fahrenheit-32) *5/9 )
    print(" ",temp,"F =  ",Celsius_temp,"C" )

temperature()

