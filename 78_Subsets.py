class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lst = []
        for i in range(len(nums)+1):
            for j in combinations(nums,i):
                lst.append(j)
        return lst
