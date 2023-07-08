class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # Define a helper function for preorder traversal with modified depth calculation
        def preorderMod(root):
            if root:
                # Recursively calculate the maximum depth of the left subtree
                left = preorderMod(root.left)
                # Recursively calculate the maximum depth of the right subtree
                right = preorderMod(root.right)
                # Return the maximum depth of the left and right subtrees plus one for the current node
                return max(left, right) + 1
            else:
                # Return 0 if the current node is None (i.e., leaf node)
                return 0
            
        # Call the preorderMod function with the root node and return the result
        return preorderMod(root)
