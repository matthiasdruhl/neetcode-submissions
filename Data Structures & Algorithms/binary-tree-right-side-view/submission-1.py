# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        level = []
        level.append(root)
        add = False

        while level:
            add = False
            lenLevel = len(level)
            for i in range(lenLevel):
                node = level.pop(0)
                if node:
                    if add == False:
                        ans.append(node.val)
                        add = True
                    level.append(node.right)
                    level.append(node.left)
        return ans
                
