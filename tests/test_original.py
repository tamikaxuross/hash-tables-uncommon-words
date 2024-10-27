from activity.original import uncommon_from_sentences
from .contains_all import contains_all

# tests
def test_gets_unique_words():
    expected = ["sweet", "sour"]
    s1 = "this apple is sweet"
    s2 = "this apple is sour"
    result = uncommon_from_sentences(s1, s2)
    assert len(expected) == len(result)
    assert contains_all(expected, result)

def test_disallow_repeat_in_same_sentence():
    expected = ["banana"]
    s1 = "apple apple"
    s2 = "banana"
    result = uncommon_from_sentences(s1, s2)
    assert len(expected) == len(result)
    assert contains_all(expected, result)
