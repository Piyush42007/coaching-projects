sentance = "python is best language"

words = sentance.split()

for word in words:
    print(word[0].upper() + word[1:], end=" ")

