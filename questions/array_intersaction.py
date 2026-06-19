"""
Q15. You are given two arrays. Without using any built-in set functions, find their intersection — elements that appear in both, without duplicates.
Input : [1, 3, 5, 7, 3, 9] and [3, 5, 5, 8, 9]
Output: [3, 5, 9]
Input : [1, 2, 2, 3] and [2, 2, 3, 4]
Output: [2, 3]
Input : [1, 2, 3] and [4, 5, 6]
Output: []
Input : [] and [1, 2, 3]
Output: []
"""

Input_list1 = [1, 3, 5, 7, 3, 9]
Input_list2 = [3, 5, 5, 8, 9]


#=======================================================================================
# ---------------------------- with using "not" ------------------------------------
#=======================================================================================
Output = []
for i in Input_list1:
    for j in Input_list2:
        if i == j:
            if i not in Output:
                Output.append(i)

print(Output)


#=======================================================================================
# ---------------------------- without using "not" ------------------------------------
#=======================================================================================
for i in Input_list1:
    for j in Input_list2:
        if i == j:
            for o in Output:
                if i == o:
                    break
print(Output)