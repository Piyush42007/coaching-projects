"""
Q. You are given a list of integers. Find the longest consecutive sequence.
Input : [100, 4, 200, 1, 3, 2]
Output: 4 (sequence: 1,2,3,4)
Input : [0, -1, 1, 2]
Output: 4 (sequence: -1,0,1,2)
Input : [5]
Output: 1
Input : [0, -1, 1, 2]
Output: 4 (sequence: -1,0,1,2)
Input : [1, 1, 1, 1]
Output: 1 (duplicates don't extend sequence)
"""

Input = [100, 4, 200, 1, 3, 2]

# with using sort()
Input.sort()

long_seq = []
long_seq.append(Input[0])
for i in Input:
    if i == (long_seq[-1] + 1):
        long_seq.append(i)
        

print(long_seq)


# without using sort()
n = len(Input)
for i in range(n):
    for j in range(i+1, n):
        if Input[i] > Input[j]:
            Input[i], Input[j] = Input[j], Input[i]

long_seq = []
long_seq.append(Input[0])
for i in Input:
    if i == (long_seq[-1] + 1):
        long_seq.append(i)
        

print(long_seq)




    


