class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        Min = [nums[0]]
        for idx in range(1, len(nums)):
            Min.append(min(Min[idx - 1], nums[idx]))
            
        Max = [nums[len(nums) - 1]] * len(nums)
        for idx in range(len(nums) - 2, -1, -1):
            Max[idx] = max(Max[idx + 1], nums[idx])
            
        for idx in range(1, len(nums) - 1):
            if Min[idx - 1] < nums[idx] < Max[idx + 1]:
                return True
        return False