def firstUniqChar(s):
    char_freq = {}
    
    # Count the frequency of each character
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    # Find the first non-repeating character
    for i, char in enumerate(s):
        if char_freq[char] == 1:
            return i
    
    return -1

# Test case 1
s1 = "leetcode"
print(firstUniqChar(s1))  

# Test case 2
s2 = "loveleetcode"
print(firstUniqChar(s2))  

# Test case 3
s3 = "aabb"
print(firstUniqChar(s3))  
