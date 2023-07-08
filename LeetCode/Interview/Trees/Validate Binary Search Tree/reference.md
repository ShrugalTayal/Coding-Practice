# Validate Binary Search Tree

## Problem Description

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

**Example 1:**

![Example 1](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)

```
Input: root = [2,1,3]
Output: true
```

**Example 2:**

![Example 2](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)

```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

**Constraints:**
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1

## Approach

To determine if a binary tree is a valid BST, we can perform an inorder traversal of the tree and check if the resulting values are in ascending order. If they are, the tree is a valid BST; otherwise, it is not.

The steps for the approach are as follows:

1. Perform an inorder traversal of the binary tree, recording the values of the nodes.
2. Check if the recorded values are in ascending order. If they are, return `True`; otherwise, return `False`.

## Complexity Analysis

The time complexity for this approach is O(n), where n is the number of nodes in the tree. This is because we need to traverse all the nodes once to perform the inorder traversal.

The space complexity is O(n) as well, considering the worst-case scenario where the binary tree is a skewed tree and the call stack for the recursive inorder traversal reaches a depth of n.

## Reference Implementation

Here's a reference implementation in Python:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(node, values):
            if node is None:
                return

            inorder(node.left, values)
            values.append(node.val)
            inorder(node.right, values)

        values = []
        inorder(root, values)

        for i in range(1, len(values)):
            if values[i] <= values[i - 1]:
                return False

        return True
```

## Summary

The "Validate Binary Search Tree" problem is solved by performing an inorder traversal of the binary tree and checking if the resulting values are in ascending order. By following this approach, we can determine if the given binary tree is a valid binary search tree.

You can find the problem and submit your solution on [LeetCode](https://leetcode.com/problems/validate-binary-search-tree/).
