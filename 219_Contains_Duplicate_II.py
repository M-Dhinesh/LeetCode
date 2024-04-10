class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        ind = {}
        for idx, x in enumerate(nums):
            if x in last_seen_index and idx - ind[x] <= k:
                return True
            ind[x] = idx
        return False
