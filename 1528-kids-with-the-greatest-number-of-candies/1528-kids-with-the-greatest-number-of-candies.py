class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        output = []
        for cn in candies:
            if cn + extraCandies >= mx:
                output.append(True)
            else:
                output.append(False)
        return output