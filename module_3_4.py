def single_root_words(root_word, *other_words):
    same_words = []
    root_lower = root_word.lower()
    for word in other_words:
        word_lower = word.lower()
        if root_lower in word_lower and word_lower != root_lower:
            same_words.append(word)
    return same_words

result1 = (single_root_words("koko", "koKO", "kokojambo", "lomm", "ijkoko","ijKokO"))
result2 = (single_root_words("urban", "UrBaN", "university.urBAN", "banan"))
print(result1)
print(result2)
