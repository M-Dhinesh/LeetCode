import math
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def add(self, prev: ListNode, curr: ListNode):
        a = prev.val
        b = curr.val
        c = math.gcd(a, b)
        d = ListNode(c, curr)
        prev.next = d
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        cur = head
        while cur and cur.next:
            self.add(cur, cur.next)
            cur = cur.next.next
        return head
