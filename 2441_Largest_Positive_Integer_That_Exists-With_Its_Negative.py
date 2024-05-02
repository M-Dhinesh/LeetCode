class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        if min(nums) > 0:
            return -1
        max = -1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == 0:
                    if max < abs(nums[i]):
                        max = abs(nums[i])
        return max
