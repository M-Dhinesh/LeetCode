class Solution:
    def isValid(self, s: str) -> bool:
        str1 = " "
        if s == "":
            return True
        if len(s) < 2:
            return False
        for i in s:
            if i == '{' or i == '[' or i == '(':
                str1 += i
                print(i)
            elif i == '}':
                if str1[-1] == '{':
                    str1 = str1[:len(str1)-1]
                else:
                    str1 +=i
            elif i == ']':
                if str1[-1] == '[':
                    str1 = str1[:len(str1)-1]
                else:
                    str1 +=i
            elif i == ')':
                if str1[-1] == '(':
                    str1 = str1[:len(str1)-1]
                else:
                    str1 +=i
        print(str1)
        return True if str1 == " " else False
                
