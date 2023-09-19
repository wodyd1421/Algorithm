class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1] * len(nums)
        answer = []
        
        for idx in range(len(nums) - 1):
            prefix.append(nums[idx] * prefix[idx])
            
        for idx in range(len(nums) - 1, 0, -1):
            suffix[idx - 1] = nums[idx] * suffix[idx]
            
        for idx in range(len(nums)):
            answer.append(prefix[idx] * suffix[idx])
            
        return answer