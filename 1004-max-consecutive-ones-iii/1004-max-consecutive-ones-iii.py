import queue

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        end = -1
        output = 0
        flip = queue.Queue()
        
        while end < len(nums) - 1:
            if nums[end + 1] == 0:
                k -= 1
                flip.put(end + 1)
                if k < 0:
                    start = flip.get() + 1
                    k += 1
            end += 1
            output = max(output, end - start + 1)
        
        return output