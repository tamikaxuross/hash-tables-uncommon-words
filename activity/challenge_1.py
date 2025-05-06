def uncommon_from_sentences_ch2(sentences):
    sentence_map = {}
    for sentence in sentences:
        count_sentence_words(sentence, sentence_map)

    return find_uncommon_ch2(sentence_map)

def count_sentence_words(sentence, sentence_map):
    seen = set()
    for word in sentence.split():
        seen.add(word)  # Only care if it appears in this sentence

    for word in seen:
        sentence_map[word] = sentence_map.get(word, 0) + 1

def find_uncommon_ch2(sentence_map):
    return [word for word, count in sentence_map.items() if count == 1]