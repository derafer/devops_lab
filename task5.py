from collections import Counter

word = input("Print your word: ")
collect = {}
test = {}
for i in range(len(word)):
    if word[i] in collect:
        collect[word[i]] = collect[word[i]] + 1
    else:
        collect[word[i]] = 1

for i in Counter(collect).most_common(3):
    print(i)
