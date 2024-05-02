class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for i in set(nums1):
            if i in nums2:            
                return i
        return -1
