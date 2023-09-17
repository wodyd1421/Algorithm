class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [vowel[0] for vowel in re.finditer('[aeiou]', s, re.I)]
        return re.sub('[aeiou]', lambda _: vowels.pop(), s, 0, re.I)