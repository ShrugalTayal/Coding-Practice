class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Use the find method to search for the occurrence of the needle in the haystack
        flag = haystack.find(needle)
        # Return the index of the first occurrence of the needle in the haystack
        return flag
