class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        sum = 0
        
        for i in range(k):
            sum += nums[i]
            
        maxAvg = sum / k
            
        for i in range(len(nums) - k):
            sum += -nums[i] + nums[i + k]
            if maxAvg < sum / k:
                maxAvg = sum / k
                
        return maxAvg