"""20. Given words = ["sun", "moon", "star", "sky"],
write code that prints only the words longer than 3 letters,
each in UPPERCASE."""

words = ["sun", "moon", "star", "sky"]

for word in words:
    if len(word) > 3:
        print(word.upper())