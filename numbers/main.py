

even = []
odd = []
prime = []

for i in range(1,11):
    if i%2 == 0:
        even.append(i)
    if i%2 != 0:
        odd.append(i)
    if i != 0 and (i%i) == 0 and (i%1) == 0:
        


print(even)
print(odd)
print(prime)
