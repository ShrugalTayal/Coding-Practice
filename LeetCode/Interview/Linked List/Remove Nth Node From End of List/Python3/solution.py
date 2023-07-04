# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        # Find the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Calculate the position of the node to be removed
        position = length - n
        
        # Reset the current node to the dummy node
        current = dummy
        
        # Move to the node just before the position
        for _ in range(position):
            current = current.next
        
        # Remove the nth node from the end
        current.next = current.next.next
        
        # Return the modified list
        return dummy.next
