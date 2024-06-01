class Solution:
    def scoreOfString(self, s: str) -> int:
        lst = [ord(i) for i in s]
        sum = 0
        for i in range(len(lst)-1):
            sum += abs(lst[i]-lst[i+1])
        return sum
        
