class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rem = (time % (n - 1)) + 1
        return rem if ((time // (n - 1)) % 2 == 0) else n - rem + 1
