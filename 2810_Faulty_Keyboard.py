class Solution:
    def finalString(self, s: str) -> str:
        temp = ""
        for i in s:
            temp = temp[::-1] if i == 'i' else temp+i
        return temp
