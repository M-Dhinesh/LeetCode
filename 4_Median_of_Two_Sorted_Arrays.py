class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = sorted((nums1 + nums2))
        n = len(lst)
        if len(lst)%2 ==0:
            return (lst[n//2] + lst[(n//2) - 1]) /2
        return lst[n//2]
