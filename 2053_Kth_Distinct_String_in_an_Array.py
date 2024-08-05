class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        lst = [i for i,j in Counter(arr).items() if j == 1 ]
        return "" if k > len(lst) else lst[k-1]
