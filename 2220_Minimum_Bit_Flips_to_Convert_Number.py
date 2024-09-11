class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = bin(start)[2:]
        goal = bin(goal)[2:] 
        cnt = 0  
        a = len(start)
        b = len(goal)
        if a > b:
            for i in range(a - b):
                goal = '0' + goal  
        elif a < b:
            for i in range(b - a):
                start = '0' + start 
        for i in range(len(start)):
            if start[i] != goal[i]:
                cnt += 1 
        return cnt      
