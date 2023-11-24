class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        array = [-1]
        
        for idx in range(len(nums)):
            
            if nums[idx] == 0:
                array += [idx]
                
        array += [len(nums)]
        max = 0
        
        if len(array) == 2:
            return len(nums) - 1
        
        for idx in range(len(array)-2):
            
            if array[idx+2] - array[idx] - 2 > max:
                max = array[idx+2] - array[idx] - 2
                
        return max