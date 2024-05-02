class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = 0
        s1 = []
        for i in s:
            if i not in s1:
                s1.append(i)
        for i in s1:
            if s.count(i) == 1:
                return s.index(i)
            cnt += 1
        return -1
