"""
Q11. You are given a list of words. Group them into anagram families.
Input:  ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
Input:  ["abc", "car", "arc", "dog", "god", "bca"]
Output: [["abc", "bca"], ["car", "arc"], ["dog", "god"]]
Input:  ["a", "b", "a"]
Output: [["a", "a"], ["b"]]

"""

_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
_output = []

for word1 in _input:
    group = []
    for word2 in _input:
        for i in word1:
            for j in word2:
                if i == j:
                    break
            else:
                break
        else:
            group.append(word2)

    ## duplicate groups in _output
    # _output.append(group)

    ## not duplicate groups in _output (without using "not")(not working yet)
    # for lst in _output:
    #     # print(lst)
    #     print(lst == group)
    #     if lst == group:
    #         break
    #     else:
    #         _output.append(group)

    ## not duplicate groups in _output (with using "not")
    if group not in _output:
        _output.append(group)

print(_output)
