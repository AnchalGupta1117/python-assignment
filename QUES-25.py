# Write a program that copies the contents of one text file to another

def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source:
            
        content = source.read()
            
    with open(destination_file, 'w') as destination:
            
        destination.write(content)
        
    print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    
source_file = 'source.txt'
destination_file = 'destination.txt'

copy_file(source_file, destination_file)
