# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        mind = math.inf
        prevc = None
        currc = None
        prev = head
        cur = head.next
        nex = cur.next
        firstc = None
        i = 1
        while(nex):
            if (nex.val > cur.val and prev.val > cur.val) or (nex.val < cur.val and prev.val < cur.val):
                if prevc == None:
                    firstc = i
                    prevc = i
                    currc = i
                else:
                    prevc = currc
                    currc = i
                    mind = min(mind,currc-prevc)
            i += 1
            prev = cur
            cur = nex
            nex = cur.next
            
        if mind == math.inf:
            return [-1,-1]
        return [mind,currc-firstc]# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        mind = math.inf
        prevc = None
        currc = None
        prev = head
        cur = head.next
        nex = cur.next
        firstc = None
        i = 1
        while(nex):
            if (nex.val > cur.val and prev.val > cur.val) or (nex.val < cur.val and prev.val < cur.val):
                if prevc == None:
                    firstc = i
                    prevc = i
                    currc = i
                else:
                    prevc = currc
                    currc = i
                    mind = min(mind,currc-prevc)
            i += 1
            prev = cur
            cur = nex
            nex = cur.next
        if mind == math.inf:
            return [-1,-1]
        return [mind,currc-firstc]
