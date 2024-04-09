class Solution(object):
    def isPalindrome(self, s):
        k = re.sub('[^a-z0-9]','',s.lower())
        return k==k[::-1]
