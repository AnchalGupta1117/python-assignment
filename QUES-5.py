def write_to_file():
    Input = input("Enter the string you want to write to the file: ")

    # Opening a text file in write mode
    with open("output.txt", "w") as file:
        
        file.write(Input)

    print("The string has been written to the file.")

write_to_file()
