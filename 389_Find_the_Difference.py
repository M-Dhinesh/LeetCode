class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum = 0
        for i in t:
            sum += ord(i) 
        for i in s:
            sum -= ord(i)
        return chr(sum)
