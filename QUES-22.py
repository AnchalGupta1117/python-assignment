#  Write a python program that returns the minimum and maximum values in a list of numbers.



def min_and_max(list):

    newList = sorted(list)
    print("sorted list is: ",newList)

    minValue = newList[0]
    maxValue = newList[-1]

    if minValue is None and maxValue is None:
        print("The list is empty.")
    else: 
        print ("minimum value is: ",minValue," maximum value is: ",maxValue)
    return 

list1 = [40,3,6,1,7,9,4,50,8,0,23,33]

min_and_max(list1)


