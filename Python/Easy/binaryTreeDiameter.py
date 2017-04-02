# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        diameter = 0
        
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        if(root == None):
            return 0
        self.depth(root);
        return self.diameter

        
        """
        :type root: TreeNode
        :rtype: int
        """

    def depth(self,root):
        leftDepth = 0 if not root.left else self.depth(root.left) + 1
        rightDepth = 0 if not root.right else self.depth(root.right) + 1

        if (leftDepth + rightDepth > self.diameter):
            self.diameter = leftDepth + rightDepth

        return leftDepth if (leftDepth > rightDepth) else rightDepth 




    
