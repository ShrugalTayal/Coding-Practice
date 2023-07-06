# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Check if the list is empty or contains only one node
        if head is None or head.next is None:
            return False
        else:
            while head is not None:
                # Check if the node value is None (visited node)
                if head.val is None:
                    return True
                else:
                    head.val = None  # Mark the node as visited
                    head = head.next  # Move to the next node
            return False
