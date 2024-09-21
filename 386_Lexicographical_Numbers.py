class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return list(map(int,sorted(map(str,[i for i in range(1,n+1)]))))
