class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] == 0:
                count += 1
                del nums[idx]
                
        for idx in range(count):
            nums.append(0)