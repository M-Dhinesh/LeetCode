class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        if n<2: return False
        mod_k={}
        prefix=0
        mod_k[0]=-1
        for i, x in enumerate(nums):
            prefix+=x
            prefix%=k
            if prefix in mod_k:
                if i>mod_k[prefix]+1:
                    return True
            else:
                mod_k[prefix]=i
        return False
