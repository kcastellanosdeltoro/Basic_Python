import random as r
import time as t


## Function for get 5000 random numbers
def random_numbers():
    return [r.randint(0,500) for i in range(5000)]

##List
list_numbers = random_numbers()
## Swapped, necessary variable to enter a while loop
swapped = True

start = t.time()
## Logic
while swapped:
    swapped = False
    for i in range(len(list_numbers) - 1):
        if list_numbers[i] > list_numbers[i + 1]:
            swapped = True
            list_numbers [i], list_numbers[i + 1] = list_numbers[i + 1], list_numbers[i]

## Result
final = t.time()
print(f"Total Time : {final - start} seconds")

