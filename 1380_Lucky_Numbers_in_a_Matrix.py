class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lst = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if min(matrix[i]) == matrix[i][j]:
                    lst1 = [matrix[k][j] for k in range(len(matrix))]
                    if max(lst1) == matrix[i][j]:
                        lst.append(matrix[i][j])
        return lst
