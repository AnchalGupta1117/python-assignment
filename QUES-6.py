def read_from_file(file_name):
        
    with open(file_name, "r") as file:
            
        content = file.read()
        print("Content of the file:")
        print(content)

        file_name = input("Enter the name of the text file: ")

read_from_file(file_name)
