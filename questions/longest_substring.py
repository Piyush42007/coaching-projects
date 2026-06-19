"""
Q. You are given a string. Find the longest substring without repeating characters.
Input : "abcabcbb"
Output: "abc" (length 3)
Input : "pwwkew"
Output: "wke" (length 3)
Input : "aaaa"
Output: "a" (length 1)
Input : ""
Output: "" (length 0)
"""

Input = "pwwkew"
Output = ""

longest_substring = ""
substring = ""

#=======================================================================================
# ---------------------------- with using "not" ------------------------------------
#=======================================================================================
for i in Input:
    if i not in substring:
        substring += i
    else:
        if len(substring) > len(longest_substring):
            longest_substring = substring
            substring = ""
            substring += i

print(longest_substring)


#=======================================================================================
# ---------------------------- without using "not" ------------------------------------
#=======================================================================================
for i in Input:
    for j in substring:
        if i == j:
            break
    else:
        if len(substring) > len(longest_substring):
            longest_substring = substring
            substring = ""
            substring += i

print(longest_substring)
