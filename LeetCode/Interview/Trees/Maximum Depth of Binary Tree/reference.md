---

## Maximum Depth of Binary Tree

**Problem Link:** [Maximum Depth of Binary Tree - LeetCode](https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/)

**Problem Description:**

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example:**

```
Input: [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7

Output: 3
```

**Note:**

A leaf is a node with no children.

**Approach:**

We can solve this problem recursively by calculating the maximum depth of the left and right subtrees and returning the maximum of the two depths plus one (for the current node).

1. If the root is `None`, return 0.
2. Calculate the maximum depth of the left subtree recursively: `left_depth = maxDepth(root.left)`.
3. Calculate the maximum depth of the right subtree recursively: `right_depth = maxDepth(root.right)`.
4. Return the maximum depth of the left and right subtrees plus one: `return max(left_depth, right_depth) + 1`.

**Complexity Analysis:**

The time complexity for this approach is O(n), where n is the number of nodes in the binary tree. We visit each node once.

The space complexity is O(h), where h is the height of the binary tree. In the worst case, the binary tree is skewed, and the height is equal to the number of nodes, resulting in O(n) space complexity. In the average case, the height of the binary tree is logarithmic in the number of nodes, resulting in O(log n) space complexity.

**Reference Implementation:**

Python:
```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
```

Java:
```java
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null)
            return 0;
        int leftDepth = maxDepth(root.left);
        int rightDepth = maxDepth(root.right);
        return Math.max(leftDepth, rightDepth) + 1;
    }
}
```

---
