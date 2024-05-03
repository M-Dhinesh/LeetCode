class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lst1 = list(map(int,version1.split(".")))
        lst2 = list(map(int,version2.split(".")))
        n = max(len(lst1),len(lst2))
        for i in range(n-len(lst1)):
            lst1.append(0)
        for i in range(n-len(lst2)):
            lst2.append(0)  
        for i in range(len(lst1)):
            if lst1[i] < lst2[i]:
                return -1
            if lst1[i] > lst2[i]:
                return 1
        return 0
