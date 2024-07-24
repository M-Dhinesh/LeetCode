class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        lst = []
        for i in nums:
            string = []
            temp = str(i)
            for j in temp:
                string.append(mapping[int(j)])
            lst.append(int("".join(map(str,string))))
        ls = list(zip(nums,lst))
        ls.sort(key = lambda x : x[1])
        return [num for num,_ in ls]
