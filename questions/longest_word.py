
sentance = "Python is best programing language. It uses interpreter to interprete"

words = sentance.split()

longest_word = ""
longest_word_len = 0

for word in words:
    strip_word = word.strip(".,")
    if len(strip_word) > longest_word_len:
        longest_word = strip_word
        longest_word_len = len(word)

print(longest_word, longest_word_len)


    