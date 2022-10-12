"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # Recursive
        if root: #if root is exist
            ans = [root.val] #start with root value
            for node in root.children:
                ans+=self.preorder(node)
            return ans
        