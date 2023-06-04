"""Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/
"""

class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverses the digits of the given integer.

        Parameters:
        - x: The integer to be reversed.

        Returns:
        The reversed integer.

        """
        x = str(x)  # Convert the integer to a string for easier manipulation
        
        if (x[0] == "-"):  # Check if the integer is negative
            x = x[1:]  # Remove the negative sign from the string
            x = "-" + x[::-1]  # Reverse the string and add back the negative sign
            x = int(x)  # Convert the reversed string back to an integer
        else: 
            x = x[::-1]  # Reverse the string representing the positive integer
            x = int(x)  # Convert the reversed string back to an integer
        
        if (x < -2**31 or x > (2**31 -1)):  # Check if the reversed integer is within the 32-bit signed integer range
            return 0  # Return 0 if it is outside the range
        else:
            return x  # Return the reversed integer
