class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dic ={}
        for i in nums:
            dic[i] = 1
        for i in range(1,max(nums)+2):
            if i not in dic:
                return i
        return 1
