class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums1, nums2 = list(nums1 - nums2), list(nums2 - nums1)
        answer = []
        answer += [nums1]
        answer += [nums2]
        return answer