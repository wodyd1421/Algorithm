class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        end = len(nums) - 1
        output = 0

        while start < end:
            if nums[start] + nums[end] == k:
                output += 1
                start += 1
                end -= 1
            elif nums[start] + nums[end] <= k:
                start += 1
            else:
                end -= 1

        return output