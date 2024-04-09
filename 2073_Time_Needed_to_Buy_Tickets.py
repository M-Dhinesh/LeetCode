class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        l = tickets[k]
        for i in range(len(tickets)):
            if tickets[i] < l:
                res += tickets[i]
            else:
                if  i <=k:
                    res += l
                else:
                    res += l-1
        return res
