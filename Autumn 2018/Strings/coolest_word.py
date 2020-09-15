def coolest_word(words):
    coolest = ''

    if words == "":
        return None
    else:
        count = 0

        for word in words:
            print(word + ' count: ' + str(count_unique_characters(word)))
            if count_unique_characters(word) > count:
                count = count_unique_characters(word)
                coolest = word

    return coolest


def count_unique_characters(word):
    char_arr = []
    for char in word:
        if char not in char_arr:
            char_arr.append(char)

    return len(char_arr)


word1 = 'thebest'  # 5
word2 = 'nothing'  # 6
word3 = 'decomposition'  # 10
word4 = 'abcdefghij'  # 10

print(coolest_word([word1, word2, word3, word4]))
