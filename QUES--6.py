# Write a program that reads the content of a text file and prints it to the console.

def read_and_print_file(file_path):
    
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)

file_path = 'file.txt'
read_and_print_file(file_path)