class Solution:
    def numSteps(self, s: str) -> int:
        cnt = 0
        target = int(s, 2)

        while target != 1:
            cnt += 1
            if target % 2 == 0:
                target = target // 2
            else:
                target += 1
        return cnt
