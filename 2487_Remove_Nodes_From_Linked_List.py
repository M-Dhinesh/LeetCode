class Solution:
    def removeNodes(self, n: Optional[ListNode]) -> Optional[ListNode]:
        if n.next:
            q = self.removeNodes(n.next)
            n.next = q
            if n.val < q.val:
                return q
        return n
