class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [vowel for vowel in re.findall('[aeiou]', s, re.I)]
        return re.sub('[aeiou]', lambda _: vowels.pop(), s, 0, re.I)