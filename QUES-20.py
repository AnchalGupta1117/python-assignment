# Write a python program that takes a list of numbers and returns their sum

def sum_list(nums):
    total = 0
    for num in nums:
        total += num
    return total
nums = [1,2,3,4,5,6]
total = sum_list(nums)

print("the sum of number in list is: ",total)