from datetime import datetime
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        min = 1441
        lst = []
        for i in timePoints:
            h,m = map(int,i.split(':'))
            mi = h*60+m
            if h < 5:
                lst.append(1440 + mi)
            lst.append(mi)
        lst.sort()
        for i in range(len(lst)-1):
            temp = abs(lst[i]-lst[i+1])
            if temp < min:
                min = temp
        return min             
