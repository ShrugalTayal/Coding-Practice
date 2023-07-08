class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        array = []
        
        def inorder(root):
            if root:
                inorder(root.left)  # Traverse the left subtree
                
                array.append(root.val)  # Append the value of the current node
                
                inorder(root.right)  # Traverse the right subtree
        
        inorder(root)  # Call the inorder traversal function to populate the array
        
        # Check if the array is in ascending order
        for i in range(1, len(array)):
            if array[i] <= array[i - 1]:  # If any value is less than or equal to its previous value
                return False

        return True
