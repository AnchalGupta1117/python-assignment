#  Write a program that asks the user for their birth year and calculates their age.

def calculate_age(birth_year):
    current_year = 2024
    current_age = current_year - birth_year
    print("your current age is: ",current_age)

BirthYear = int(input("enter your birth year: "))

calculate_age(BirthYear)