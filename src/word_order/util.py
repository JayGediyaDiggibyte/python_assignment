
def word_order(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return len(word_count), list(word_count.values())