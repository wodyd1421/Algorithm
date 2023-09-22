class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        count = 1
        start = 0
        chars.append(-1)
        while start != len(chars) and idx != len(chars) - 1:
            if chars[idx + 1] == chars[idx]:
                count += 1
            else:
                chars[start] = chars[idx]
                if count == 1:
                    start += 1
                else:
                    for i, numstr in enumerate(list(str(count))):
                        chars[start + i + 1] = numstr
                    start += len(str(count)) + 1
                    count = 1
            idx += 1
        chars = chars[:start]
        return len(chars)