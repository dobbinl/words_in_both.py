def words_in_both(s1, s2):
    """
    Program takes two strings; changing to lowercase letters.
    :Split funtion breaks up string in to two lists.
    """
    s1 = s1.lower()
    s2 = s2.lower()

    words1 = s1.split()
    words2 = s2.split()
    print(words1)
    print(words2)
    words_set1 = set(words1)
    words_set2 = set(words2)
    common_words = words_set1.intersection(words_set2)
    return common_words