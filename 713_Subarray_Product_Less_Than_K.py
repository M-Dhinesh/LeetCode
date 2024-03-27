class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        curr = 1
        left = ans = 0
        for right in range(len(nums)):
            curr = curr * nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1
            ans = ans + right - left + 1
        return ans

        
