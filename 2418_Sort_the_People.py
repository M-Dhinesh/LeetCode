class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        lst = list(zip(heights,names))
        lst.sort(reverse = True, key = lambda x : x[0])
        return [name for _,name in lst]
