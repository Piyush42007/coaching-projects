
para = "Python is best programming language. Python uses interpreter to interprete the code.it uses to code llms and ai models "
para_lower = para.lower()


max_count = {"word":"", "count":0}
for word1 in para_lower:
    word_count = 0
    if word1 != " ":
        for word2 in para_lower:
            if word1 == word2:
                word_count += 1

        if word_count > max_count["count"]:
            max_count["word"] = word1
            max_count["count"] = word_count

print(max_count)










