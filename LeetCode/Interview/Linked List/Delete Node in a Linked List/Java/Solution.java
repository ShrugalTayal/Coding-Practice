/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        // Get the reference to the next node
        ListNode nextNode = node.next;

        // Copy the value of the next node to the current node
        node.val = nextNode.val;

        // Skip the next node by updating the next pointer of the current node
        node.next = nextNode.next;
    }
}
