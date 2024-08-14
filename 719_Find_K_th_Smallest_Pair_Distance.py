class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int: 
        return sorted([abs(i[0]-i[1]) for i in combinations(nums,2)])[k-1]
