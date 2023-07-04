/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // Create a dummy node to handle edge cases
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        // Initialize current node and length counter
        ListNode current = head;
        int length = 0;
        
        // Traverse the linked list to calculate its length
        while (current != null){
            length++;
            current = current.next;
        }
        
        // Reset current to the beginning of the list
        current = dummy.next;
        
        // Calculate the position of the node to be removed
        int position = length - n;
        System.out.println(position);
        
        // Traverse to the (position-1)th node
        for (int i=0; i<position-1; i++){
            current = current.next;
        }

        // Remove the nth node from the end by skipping it
        if (position != 0){
            current.next = current.next.next;
        }
        else {
            // If the first node is to be removed, update the dummy node
            dummy.next = current.next;
        }
        
        // Return the updated list
        return dummy.next;
    }
}
