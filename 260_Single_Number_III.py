class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a = Counter(nums)
        lst = []
        for i in a.keys():
            if len(lst) == 2:
                break
            if a[i] == 1:
                lst.append(i)
        return lst
            
        
