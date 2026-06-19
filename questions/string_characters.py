
# string_1 = (input("Enter string: ")).lower()
string_1 = "programming"

#-------------------- 1st method without "not"---------------------

# sorted_string = ""
# for i in string_1:
#     if i not in sorted_string:
#         sorted_string += i
# print(sorted_string)


#-------------------- 2nd method without "not"---------------------

sorted_string = ""
for i in string_1:
    for j in sorted_string:
        if i == j:
            break
    else:
        sorted_string += i
print(sorted_string)







