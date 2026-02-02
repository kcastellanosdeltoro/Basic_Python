import random as r
import time as t

## Function for get 5000 random numbers
def random_numbers():
    return [r.randint(0,500) for i in range(5000)]

##List
list_numbers = random_numbers()

start = t.time()
## Logic
for i in range(len(list_numbers) - 1):
    minimum = i
    for j in range(i + 1, len(list_numbers)):
        if list_numbers[j] < list_numbers[minimum]:
            minimum = j

    #Swapped
    list_numbers[i], list_numbers[minimum] = list_numbers[minimum], list_numbers[i]

## Result
final = t.time()
print(f"Total Time : {final - start} seconds")