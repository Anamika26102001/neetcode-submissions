# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root,subRoot):
            return True
        if self.isSubtree(root.left,subRoot):
            return True
        if self.isSubtree(root.right, subRoot):
            return True
        return False


    
    def sameTree(self, p, q ):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if(p.val!=q.val):
            return False
        if not self.sameTree(p.left,q.left):
            return False
        if not self.sameTree(p.right,q.right):
            return False

        return True