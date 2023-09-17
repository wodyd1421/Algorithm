class Solution:
    def reverseVowels(self, s: str) -> str:
        word = list(s)
        start = 0
        end = len(word) - 1
        vowels = 'aeiouAEIOU'
        
        while start < end:
            if word[start] not in vowels:
                start += 1
                continue
            
            if word[end] not in vowels:
                end -= 1
                continue
            
            word[start], word[end] = word[end], word[start]
            start += 1
            end -= 1
                
        return ''.join(word)