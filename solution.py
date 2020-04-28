
# Given a binary tree, return true if it is balanced or false otherwise. 
# You can assume that all of the data is unique. A balanced tree is defined as following:

# it’s left subtree is balanced
# it’s right subtree is balanced
# the height of its two subtrees can differ by 1 or 0

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Input: a binary tree 
# Output: the height of the tree. 
def getHeight(self, node: TreeNode) -> bool:
    
    #check edge case if tree is null.
    if node is None:
        return 0
    
    #traverse both left and right of the tree recursively 
    left = self.getHeight(node.left)
    right = self.getHeight(node.right)
    
    #compares both heights and returns the height of the highest subtree.
    if left > right:
        return left + 1
    else:
        return right +1
    
#Input: a binary tree 
# Output: true if balanced, flase otherwise. 
def isBalanced(self, root: TreeNode) -> bool:
    #check edge case when tree is None.
    if root is None:
        return True 
    
    # obtains the height of both left and right subtrees
    if abs((self.getHeight(root.left) - self.getHeight(root.right))) > 1:
        return False
    
    #traverse both sides checking that 
    # does not violate the property of a balanced tree. 
    return self.isBalanced(root.left) and self.isBalanced(root.right)

# Explanation: In order for us to check if the given tree is a balanced tree, we need to check 2 things. 
# First that both the right and left subtree are balanced and second, that the difference of heights of its subtrees
# is no greater than one. For that reason, we create an auxiliary method to obtain the height of a given tree. 
# This method traverses the tree acummulating and comparing the branches looking for the highest height. 
# Then we have a method to check that uses the height of the tree to check if it is balanced. This checks if the 
# node is null, then obtains the height of both left and right subtrees and traverses both sides checking that 
# does not violate the property of a balanced tree. If both subtrees are balanced then the tree is balanced. 

# Time Complexity ~ O(n)
# Space Complexity ~ O(1)