
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))



if num_1 < num_2:
    a = num_1
    b = num_2
else:
    a = num_2
    b = num_1

numbers = []
for num in range(a,b+1):
    if num%2 != 0:
        numbers.append(num)

print(numbers)