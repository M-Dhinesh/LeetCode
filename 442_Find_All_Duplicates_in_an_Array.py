class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicatemap={}
        for i in nums:
            if(i in duplicatemap):
                duplicatemap[i]+=1
            else:
                duplicatemap[i]=1
        return [k for k,v in duplicatemap.items() if v>1]
