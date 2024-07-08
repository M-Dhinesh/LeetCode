class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def recursion(n, k):
            if n == 1:
                return 0
            return (recursion(n - 1, k) + k) % n
        return recursion(n, k) + 1
