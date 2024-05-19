from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        key1 = Counter(word1).keys()
        key2 = Counter(word2).keys()
        if key1 != key2:
            return False
        word1 = sorted(list(Counter(word1).values()))
        word2 = sorted(list(Counter(word2).values()))
        if word1 == word2:
            return True
        return False