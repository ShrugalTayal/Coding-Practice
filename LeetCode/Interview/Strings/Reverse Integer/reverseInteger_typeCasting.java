/*Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/
*/

class Solution {
    public int reverse(int x) {
        /**
         * Reverses the digits of the given integer.
         *
         * @param x The integer to be reversed.
         * @return The reversed integer.
         */
        String s = Integer.toString(x); // Convert the integer to a string for easier manipulation
        
        if (s.charAt(0) == '-') { // Check if the integer is negative
            s = s.substring(1); // Remove the negative sign from the string
            s = "-" + new StringBuilder(s).reverse().toString(); // Reverse the string and add back the negative sign
            
        } else {
            s = new StringBuilder(s).reverse().toString(); // Reverse the string representing the positive integer
        }
        
        long l = Long.parseLong(s); // Convert the reversed string back to a long
        
        if (l < -Math.pow(2, 31) || l > Math.pow(2, 31)) { // Check if the reversed integer is within the 32-bit signed integer range
            x = (int) l; // Store the reversed integer as an int
            return 0; // Return 0 if it is outside the range
        } else {
            x = (int) l; // Store the reversed integer as an int
            return x; // Return the reversed integer
        }
    }
}
