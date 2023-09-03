class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ''
        Min = min(len(word1), len(word2))
        for idx in range(Min):
            answer += word1[idx] + word2[idx]
        if len(word1) > Min:
            for idx in range(Min, len(word1)):
                answer += word1[idx]
        if len(word2) > Min:
            for idx in range(Min, len(word2)):
                answer += word2[idx]
        return answer