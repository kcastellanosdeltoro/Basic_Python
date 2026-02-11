# Given two list, return a list with the elements appears in both list (without duplicates)
import random


list_one = [random.randint(0,10) for i in range(6)]
list_two = [random.randint(0,10) for i in range(6)]
new_list = [] 

for i in list_one:
    for j in list_two:
        if i == j and i not in new_list:
            new_list.append(i)

print(list_one)
print(list_two)
print(new_list)