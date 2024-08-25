# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

    #thought:
        #we navigate through tree in preorder, if we find a node that matches subroots head we run sametree if True we return True else we ckeep navigating

        if root:
            #match found, run sameTree
            if root.val == subRoot.val:
                if self.sameTree(root, subRoot):
                    return True
            
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def sameTree(self, root1, root2):
        
        #win case
        if root1 is None and root2 is None:
            return True
        #implement breaks first
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False

        return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)
