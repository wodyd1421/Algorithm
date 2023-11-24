class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = 0
        rightsum = sum(nums) - nums[0]
        if rightsum == 0:
            return 0
        for idx in range(len(nums)-1):
            leftsum += nums[idx]
            rightsum -= nums[idx+1]
            if leftsum == rightsum:
                return idx+1
        return -1