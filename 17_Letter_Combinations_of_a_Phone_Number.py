class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dial = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        r = [""] if digits != "" else []
        for i in range(len(digits)):
            r = [p + q for p in r for q in dial[int(digits[i])]]
        return r
