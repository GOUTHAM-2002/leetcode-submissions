# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        found=False
        subroot=subRoot
        def preorder(main):
            nonlocal found
            if not main:
                return
            if main.val==subRoot.val:
                meow = equal(main,subroot)
                if meow:
                    found=meow
            preorder(main.left)
            preorder(main.right)
        def equal(main,subroot):
            if not main and subroot or main and not subroot:
                return False
            if not main and not subroot:
                return True
            if main.val!=subroot.val:
                return False
            return equal(main.left,subroot.left) and equal(main.right,subroot.right)
        preorder(root)
        return found

        