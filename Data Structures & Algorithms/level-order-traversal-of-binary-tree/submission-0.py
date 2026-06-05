# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=[root]
        res=[]
        def bfs():
            if not q:
                return
            length = len(q)
            temp=[]
            for _ in range(length):
                meow = q.pop(0)
                temp.append(meow.val)
                if meow.left:
                    q.append(meow.left)
                if meow.right:
                    q.append(meow.right)
            res.append(temp)
            bfs()
        bfs()
        return res

        