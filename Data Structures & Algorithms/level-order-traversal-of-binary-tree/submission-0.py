# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        que = []
        que.append(root)

        while que:
            qLen = len(que)
            tempArr = []
            for i in range(qLen):
                node = que.pop(0)
                if node:
                    tempArr.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
            if len(tempArr) > 0:
                ans.append(tempArr)
        return ans
            