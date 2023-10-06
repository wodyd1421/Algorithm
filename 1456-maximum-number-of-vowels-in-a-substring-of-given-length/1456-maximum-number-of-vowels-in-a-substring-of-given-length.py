class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s += 'z'
        Max = 0
        
        for n in range(k):
            
                if s[n] in 'aeiou':
                    Max += 1
                    
        output = Max
        
        for i in range(len(s) - k):
            
            if s[i] in 'aeiou':
                Max -= 1
                
            if s[i + k] in 'aeiou':
                Max += 1
                
            output = max(output, Max)
            
        return output