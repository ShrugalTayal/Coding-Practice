"""First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Finds the index of the first non-repeating character in a given string.

        Parameters:
        - s: The input string.

        Returns:
        The index of the first non-repeating character, or -1 if all characters are repeating.

        """
        for ele in s:  # Iterate through each character in the string
            if (s.count(ele) == 1):  # Check if the character count is equal to 1, indicating it is non-repeating
                return s.index(ele)  # Return the index of the first non-repeating character
        else:
            return -1  # Return -1 if all characters are repeating
