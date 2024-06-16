# Write a program in python that checks if a string starts with a given prefix or ends with a given suffix

def prefix(prfx,string):
    for el in prfx:
        for i in string:
            if el == i:
                return True
            else:
                return False
            
def suffix(sufx,string):
        if string.endswith(sufx):
             return True
        else:
            return False


def function():
    str1 = input("Enter a string: ")
    print("1. check for prefix")
    print("2. check for suffix")
    choice = input("enter your choice(1 or 2): ")
    if choice == "1":
        prfix = input("enter the prefix: ")
        prefix(prfix,str1)
        if prefix(prfix,str1) == True:
            print("The string {",str1,"} starts with prefix {",prfix, "}")
        else:
                print("The string {",str1,"} does not starts with prefix {",prfix, "}")
            
           
        
    elif choice == "2":
        sufix = input("enter the suffix: ")
        suffix(sufix,str1)
        if suffix(sufix,str1) == True:
            print("The string {",str1,"} ends with suffix {",sufix,"}")
        else:
            print("The string {",str1,"} does not ends with suffix {",sufix, "}")
        return
function()
