# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head != None and head.next != None:
            # Initialize previous, current, and next nodes
            prev = head
            current = prev.next
            next = current.next

            print(prev, current, next)

            # Disconnect the head from the reversed list
            prev.next = None

            # Reverse the list by adjusting the pointers
            while current != None and current.next != None:
                current.next = prev
                prev = current
                current = next
                if current.next != None:
                    next = current.next
                else:
                    break

            # Connect the last node to the reversed list
            current.next = prev

            # Update the head as the last node in the reversed list
            head = current
            return head

        else:
            # Return the input head if it is None or has only one node
            return head
