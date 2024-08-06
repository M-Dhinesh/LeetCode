class Solution:
    def minimumPushes(self, word: str) -> int:
        counter_sorted = sorted(Counter(word).values(), reverse=True)   
        return sum(counter_sorted[:8]) + 2*sum(counter_sorted[8:16]) + 3*sum(counter_sorted[16:24]) + 4*sum(counter_sorted[24:])
