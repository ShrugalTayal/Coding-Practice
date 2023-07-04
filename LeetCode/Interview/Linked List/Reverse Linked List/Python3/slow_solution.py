# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head != None:
            # Create an empty list to store the nodes
            List = []
            
            # Traverse the linked list and append each node to the list
            current = head
            while current:
                List.append(current)
                current = current.next
            
            # Reverse the list of nodes
            List.reverse()
            
            # Get the tail node and disconnect it from the reversed list
            tail = List[-1]
            tail.next = None
            
            # Reconnect the nodes in the reversed order
            for index in range(-1, -len(List), -1):
                List[index-1].next = List[index]
            
            # Update the head node as the first node in the reversed list
            head = List[0]
            return head
        else:
            # Return the input head if it is None
            return head
