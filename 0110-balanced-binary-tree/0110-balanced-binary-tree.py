class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        
        def _isBalanced(node):
            if not node:
                return 0
            
            leftHeight = _isBalanced(node.left)        
            rightHeight = _isBalanced(node.right)

            if leftHeight is False or rightHeight is False:
                return False 

            if abs(leftHeight - rightHeight) > 1:
                return False 

            return 1 + max(leftHeight, rightHeight)
        
        return _isBalanced(root)