# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, parent):
        if node is None:
            return
        node.parent = parent
        if node.val in self.toDel:
            self.nodes.pop(node.val)
            if parent:
                if parent.left and parent.left.val == node.val:
                    parent.left = None
                if parent.right and parent.right.val == node.val:
                    parent.right = None
            self.helper(node.left, None)
            self.helper(node.right, None)
            return
        self.helper(node.left, node)
        self.helper(node.right, node)
    def traverse(self, node, parent):
        if node is None:
            return
        self.nodes[node.val] = node
        node.parent = parent
        self.traverse(node.left, node)
        self.traverse(node.right, node)
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.toDel = set(to_delete)
        self.nodes = {}
        self.traverse(root, None)
        self.helper(root, None)
        return [node for node in self.nodes.values() if not node.parent]
