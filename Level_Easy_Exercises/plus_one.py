# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

def plus_one(digits):
    number = ''
    new_list = []

    for i in digits:
        number += str(i)
    
    number = int(number) + 1
    number = str(number)
    
    for i in number:
        new_list.append(int(i))

    return new_list

print(plus_one([4,3,2,1]))
