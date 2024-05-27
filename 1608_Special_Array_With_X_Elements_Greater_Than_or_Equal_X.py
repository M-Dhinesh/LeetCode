class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for n in range(len(nums)+1):
            cnt = 0
            for i in nums:
                if i >= n:
                    cnt += 1
            if cnt == n: 
                return cnt
        return -1
