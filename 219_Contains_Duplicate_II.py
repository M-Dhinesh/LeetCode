class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        ind = {}
        for idx, x in enumerate(nums):
            if x in ind and idx - ind[x] <= k:
                return True
            ind[x] = idx
        return False
