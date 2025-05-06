def uncommon_from_sentences(sentences):
    counts = {}
    for sentence in sentences:
        count_words(sentence, counts)  # Count each word once per sentence

    return find_uncommon(counts)  # Return words that only appeared in one sentence

def count_words(sentence, counts):
    for word in set(sentence.split()):  # Use set to avoid double-counting in one sentence
        counts[word] = counts.get(word, 0) + 1

def find_uncommon(counts):
    return [word for word, count in counts.items() if count == 1]