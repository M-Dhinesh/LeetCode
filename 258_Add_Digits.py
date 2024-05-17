class Solution:
    def addDigits(self, num: int) -> int:
        nums = list(str(num))
        if len(nums) == 1:
            return int(nums[0])
        else:
            return self.addDigits(int(str(sum(list(map(int,nums))))))
