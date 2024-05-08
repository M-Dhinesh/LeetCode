class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dic = {}
        lst = []
        a = sorted(score,reverse = True)
        for i in a:
            dic[i] = str(a.index(i) +1)
        for i,j in dic.items():
            if j == "1":
                dic[i] = "Gold Medal"
            elif j == "2":
                dic[i] = "Silver Medal"
            elif j == "3":
                dic[i] = "Bronze Medal"
        for i in score:
            lst.append(dic[i])
        return lst
