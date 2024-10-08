# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def pot(root):    
            if root is None:
                return
            result.append(root.val)
            pot(root.left)
            pot(root.right)
        pot(root)

        return result
