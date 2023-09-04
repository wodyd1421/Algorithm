class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in reversed(range(len(str1))):
            part = str1[:i + 1]
            if str1 == part * int(len(str1) / len(part)):
                if str2 == part * int(len(str2) / len(part)):
                    return part
        return ''