def uncommon_from_sentences(first, second):
    word_counts = {}
    count_words(first, word_counts)
    count_words(second, word_counts)
    return get_uncommon_words(word_counts)

def count_words(sentence, word_counts):
    for word in sentence.split():
        word_counts[word] = word_counts.get(word, 0) + 1

def get_uncommon_words(word_counts):
    return [word for word, count in word_counts.items() if count == 1]