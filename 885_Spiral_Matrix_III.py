class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        traversed = []
        step, direction = 1, 0 
        while len(traversed) < R * C:
            for _ in range(2):
                for _ in range(step):
                    if r0 >= 0 and r0 < R and c0 >= 0 and c0 < C:
                        traversed.append([r0, c0])
                    r0 += dirs[direction][0]
                    c0 += dirs[direction][1]
                direction = (direction + 1) % 4
            step += 1
        return traversed
