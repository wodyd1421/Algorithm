class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for idx in range(len(s)):
            if t.find(s[idx]) != -1:
                i = t.find(s[idx])
                if idx == len(s) - 1:
                    return True
            else:
                return False
            if i == len(t) - 1:
                return False
            t = t[i + 1:]
        return True