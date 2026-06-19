"""
Q. You are given a paragraph. Find the longest palindromic substring in it (ignore spaces and punctuation).
Input : "never odd or even"
Output: "neveroddoreven"
Input : "racecar is a word"
Output: "racecar"
Input : "abcd"
Output: any single character (no palindrome longer than 1)
Input : "a"
Output: "a"
"""

Input = "racecar is a word"
string = ""
for i in Input:
    if i == " ":
        continue
    else:
        string += i


long_palindrome = ""
palindrome = ""
for i in range(len(string)+1):

    if string[:i] == string[:i][::-1]:
        palindrome = string[:i]
    
    if palindrome > long_palindrome:
        long_palindrome = palindrome


print(long_palindrome)




