def single_root_words(root_word, *other_word):
    same_words = []
    for word in other_word:
        if root_word.lower in other_word.lower or other_word.lower in root_word.lower:
            same_words.append(word)
            return same_words
a = single_root_words()
print(a)
print(same_words)