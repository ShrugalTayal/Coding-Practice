"""Reverse String
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses the given string in-place.

        Parameters:
        - s: The list of characters representing the string to be reversed.

        Returns:
        None. The string is modified in-place.

        """
        print(s.reverse())  # Reverse the string in-place and print the result.
