/*Reverse String
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
*/
class Solution {
    public void reverseString(char[] s) {
        // Iterate over the first half of the array
        for (int i=0; i<(s.length)/2; i++) {
            char temp; // Temporary variable to store the current character
            temp = s[i]; // Store the current character in temp
            
            // Swap the current character with its corresponding character from the end of the array
            s[i] = s[s.length - 1 - i]; 
            s[s.length - 1 - i] = temp;
        }
        // No need to return s since the array is modified in-place
    }
}
