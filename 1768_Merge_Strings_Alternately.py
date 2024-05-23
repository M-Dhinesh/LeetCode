class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        maxi = min(len(word1),len(word2))
        word = ""
        for i in range(maxi):
            word += (word1[i] + word2[i])
        if len(word1) != maxi:
            word += word1[maxi:]
        else:
            word += word2[maxi:]
        return word
