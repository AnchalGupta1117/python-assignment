# Write a python program that removes all punctuation from a given string

# def remove_punctuation():
#     str = input("enter a string: ")
#     str1 = str.replace(",","")
#     str2 = str1.replace(".","")
#     str3 = str2.replace("?","")
#     str4 = str3.replace("!","")
#     str5 = str4.replace(":","")
#     str6 = str5.replace(";","")
#     str7 = str6.replace("'","")
#     str8 = str7.replace('"',"")
#     str9 = str8.replace("(","").replace(")","")
#     str10 = str9.replace("-","")
#     str11 = str10.replace("_","")
#     str12 = str11.replace("-","")
#     str13 = str12.replace("[","").replace("]","")
#     str14 = str13.replace("{","").replace("}","")
#     str15 = str14.replace("/","")
#     print("final string is: ",str15)

# remove_punctuation()

def remove_punctuation():
    str = input("enter a string: ")
    list1 = list(str)
    list2 = ["!",",",".","/","?",":",";","'",'"',"{","}","[","]","_","-",")","(","^"]
    for i in list2 :
        for el in list1 :
            if i == el:
                list1.remove(el)
            else: list1
    str1 = ''.join(list1)
    print(str1)

remove_punctuation()



    