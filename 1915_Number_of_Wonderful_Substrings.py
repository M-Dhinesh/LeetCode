class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        toBit = {c: 1 << i for i, c in enumerate(ascii_lowercase[:])}
        print(*enumerate(ascii_lowercase[:]))
        print(toBit)
        mask = 0

        count = defaultdict(int)
        count[0] = 1

        for c in word:
            mask ^= toBit[c]
            count[mask] += 1

        res = 0
        for mask, cnt in count.items():
            res += cnt * (cnt - 1) // 2
            for i in range(10):
                mask2 = mask ^ (1 << i)
                if mask2 < mask:
                    res += cnt * count.get(mask2, 0)
        return res
