# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def checkNode(node1, node2):
            if not node1 and not node2:
                return True

            if node1 and node2 and node1.val == node2.val:
                return checkNode(node1.left, node2.left) and checkNode(node1.right, node2.right)

         
            
            return False
        
        def checkRoots(node, subRoot):
            if not node:
                return False
            if node.val == subRoot.val:
                if checkNode(node, subRoot):
                    return True
                
            return checkRoots(node.left, subRoot) or checkRoots(node.right, subRoot)

        
        return checkRoots(root, subRoot)