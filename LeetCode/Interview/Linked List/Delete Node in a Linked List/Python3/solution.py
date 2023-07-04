# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:            
    def deleteNode(self, node):
        """
        Deletes a node from a singly-linked list.
        
        :param node: The node to be deleted.
        :type node: ListNode
        :rtype: None
        """
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next
        del next_node
