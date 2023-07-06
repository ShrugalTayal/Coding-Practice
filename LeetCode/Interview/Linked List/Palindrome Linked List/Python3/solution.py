# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = []  # Initialize a list to store the values of the linked list
        
        # Traverse the linked list and store the values in the list
        while head is not None:
            list.append(head.val)
            head = head.next
        
        # Check if the list is equal to its reverse
        return list == list[::-1]
