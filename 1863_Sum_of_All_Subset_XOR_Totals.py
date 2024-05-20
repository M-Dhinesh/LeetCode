class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sum = 0
        for i in range(1,len(nums)+1):
            for j in combinations(nums,i):
                xor = 0
                for k in j:   
                    xor ^= k
                sum += xor
        return sum
