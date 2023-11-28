from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        Set = set(counter.values())
        if len(counter) == len(Set):
            return True
        return False