class Solution:
    def removeStars(self, s: str) -> str:
        stack = list()
        for i in range(len(s)):
            if s[i] != '*':
                stack.append(s[i])
            else:
                del stack[-1]
        return ''.join(stack)