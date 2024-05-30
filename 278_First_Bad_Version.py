class Solution:
    def firstBadVersion(self, n):
        i = 1
        j = n
        while (i < j):
            temp = (i+j) // 2
            if (isBadVersion(temp)):
                j = temp       
            else:
                i = temp + 1   
        return i
