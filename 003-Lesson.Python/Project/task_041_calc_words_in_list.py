words_result = dict()
words = ["aaa", "bbb", "aaa", "ccc", "ddd", "aaa", "rrr", "aaa", "ccc"]

for word in words:
    if word in words_result.keys():
        words_result[word] += 1
    else:
        words_result[word] = 1

print(words_result)
