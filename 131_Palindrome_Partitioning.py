class Solution:
    def __init__(self):
        self.ans = {}
        
    def partition(self, s: str) -> List[List[str]]:
        if(s in self.ans):
            return self.ans[s]
        
        if(len(s) == 0):
             result = [[]]
        elif(len(s) == 1):
             result = [[s]]
        else:
            result = []
            for i in range(1, len(s) + 1):  
                left = []
                if(s[:i] == "".join(reversed(s[:i]))):
                    left.append([s[:i]])

                right = self.partition(s[i:])

                for l in left:
                    for r in right:
                        result.append(l + r)
        
        self.ans[s] = result
        return result
