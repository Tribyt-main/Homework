def single_root_words(root_word, *other_words):
    same_words = []
    for words in other_words:
        if words.lower() in root_word.lower() or root_word.lower() in words.lower():
            same_words.append(words)
    return same_words


result1 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result2 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)
print(result2)
