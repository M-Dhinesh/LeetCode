class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        temp = len(nums)
        for i in nums:
            if i >= target:
                temp = nums.index(i)
                break
        return temp
