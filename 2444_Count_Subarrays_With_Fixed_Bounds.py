class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        min_index, max_index, bad_index = -1, -1, -1
        for i, v in enumerate(nums):
            if v < minK or v > maxK:
                min_index, max_index, bad_index = -1, -1, i
            if v == minK:
                min_index = i
            if v == maxK:
                max_index = i
            
            if min_index > -1 and max_index > -1:
                res += min(min_index, max_index) - bad_index
        return res
