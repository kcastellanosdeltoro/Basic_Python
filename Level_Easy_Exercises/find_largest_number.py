#Find the largest number from list 
import random

def random_numbers():
    return [random.randint(0,1000) for i in range(51)]

my_list = random_numbers()

def find_largest_number(my_list):
    longest_number = my_list[0]
    for i in my_list:
        if longest_number < i:
            longest_number = i
    return longest_number

print(f"List : {my_list}")
print(f"The Largest Number From List Is : {find_largest_number(my_list)}")