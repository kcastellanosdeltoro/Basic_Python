# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

strs = ["flower","flow","flight"]
prefix = strs[0]

for i in range(1, len(strs)):
    next_word = strs[i]

    while not next_word.startswith(prefix):
        prefix = prefix[:-1]
        if not prefix:
            break
        
print(prefix)