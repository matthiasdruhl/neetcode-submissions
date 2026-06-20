# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # DFS
        #   Check if left node
        #       if so dfs(left)
        #       if dfs(left) length = k:
        #           return dfs(left)
        #       append node to end
        #   Check if right node
        #       if so dfs(right)
        #       extend dfs(right) + node
        #   return node

        def dfs(node):
            temp = [node.val]
            if not node.left and not node.right:
                return temp
            
            
            
            if node.left:
                left = dfs(node.left)
                
                left.extend(temp)
                temp = left
        
            if node.right:
                right = dfs(node.right)
                temp.extend(right)
            return temp

        res = dfs(root)
        return res[k - 1]

        




            

