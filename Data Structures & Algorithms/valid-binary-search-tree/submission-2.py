# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack=[]
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            stack.append(root.val)
            inorder(root.right)
        inorder(root)
        meow=stack[0]
        for i in range(1,len(stack)):
            if stack[i]<=meow:
                return False
            meow=stack[i]
        return True
            

        