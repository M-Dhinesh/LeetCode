import numpy as np
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = []
        mat = np.array(grid)
        for i in range(len(mat)-2):
            t = []
            for j in range(len(mat[0])-2):
                t.append(max(mat[i:i+3, j:j+3].reshape(-1)))
            res.append(t)
        return res
