class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                return num
