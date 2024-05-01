class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = 0
        for i in range(len(word)):
            if word[i] == ch:
                n = i
                break
        if n == 0:
            return word
        return word[0:n+1][::-1]+word[n+1:]
