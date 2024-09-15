class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        def vowel(s1):
            alpha = {'a':0,'e':0,'i':0,'o':0,'u':0}
            for i in s1:
                if i in ['a','e','i','o','u']:
                    alpha[i] += 1
            return all(i % 2 == 0 for i in alpha.values())
        for j in range(len(s),0,-1):
            for i in range(len(s)):
                if len(s) >= i+j:
                    s1 = s[i:i+j]
                    if vowel(s1):
                        return(len(s1))
        return 0
