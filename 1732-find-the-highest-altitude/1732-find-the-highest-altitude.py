class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        Max, alt = 0, 0
        for gain in gain:
            alt += gain
            Max = max(Max, alt)
        return Max