# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, lower_b, upper_b):
            
            if not node:
                return True
            
            if node.left:
                print(node.left.val, lower_b, upper_b)
                if node.left.val >= node.val or node.left.val >= upper_b or node.left.val <= lower_b:
                    return False
            if node.right:
                if node.right.val <= node.val or node.right.val <= lower_b or node.right.val >= upper_b :
                    
                    return False
            return isValid(node.left, lower_b, node.val) and isValid(node.right, node.val, upper_b)
    
        return isValid(root, -1000, 1000)