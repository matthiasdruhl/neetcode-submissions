# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pSet = set()
        qStack = []

        def findp(node, p):
            nonlocal pSet
            if not node:
                return False
            if node.val == p.val:
                pSet.add(node)
                return True
            if findp(node.left, p) or findp(node.right, p):
                pSet.add(node)
                return True
            return False

        def findq(node, q):
            nonlocal qStack
            if not node:
                return False
            if node.val == q.val:
                qStack.append(node)
                return True
    
            if findq(node.left, q) or findq(node.right, q):
                qStack.append(node)
                return True
            return False
        
        findp(root, p)
        findq(root, q)

        while True:
            temp = qStack.pop(0)
            print(temp.val)
            if temp in pSet:
                return temp
        

            