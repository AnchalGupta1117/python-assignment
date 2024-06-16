#  Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.

def read_and_print_user_input():
    lines = []
    print("Enter multiple lines of text. To finish, just press Enter on an empty line.")

    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    print("\nYou entered:")
    for line in lines:
        print(line)

read_and_print_user_input()
