class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = {'5':0,'10':0,'20':0}
        for i in bills:
            if i == 5:
                dic['5'] += 1
            elif i == 10:
                if dic['5'] > 0:
                    dic['10'] += 1
                    dic['5'] -= 1
                else: 
                    return False
            else:
                if dic['5'] > 0:
                    if dic['10'] > 0:
                        dic['20'] -= 1
                        dic['10'] -= 1
                        dic['5'] -= 1
                    elif dic['5'] > 2:
                        dic['20'] -= 1
                        dic['5'] -= 3
                    else: 
                        return False
                else:
                    return False
        return True    
                

