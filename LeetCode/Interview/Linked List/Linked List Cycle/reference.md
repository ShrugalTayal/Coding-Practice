---

## Linked List Cycle

**Problem Description:**

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

LeetCode Link: [Linked List Cycle](https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/)

**Example 1:**

Input: `head = [3,2,0,-4]`
- Node with value 3 is connected to Node with value 2, forming a cycle.

Output: `true`

**Example 2:**

Input: `head = [1,2]`
- Node with value 1 is connected to Node with value 2, forming a cycle.

Output: `true`

**Example 3:**

Input: `head = [1]`
- The linked list only has one node, which does not form a cycle.

Output: `false`

**Constraints:**

- The number of nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked-list.

---

The problem "Linked List Cycle" requires determining whether a given linked list contains a cycle. The input is the head of the linked list, and the task is to check if there is a cycle within the list. A cycle is formed when a node in the list points to a previously visited node.
