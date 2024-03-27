import math
class Solution:
    def reverse(self, x: int) -> int:
        a =0
        if x>0:
            a = int(str(abs(x))[::-1])  
        else:
            a = -int(str(abs(x))[::-1])
        if a >= 2147483647 or a <= -2147483648:
            return 0
        return a
