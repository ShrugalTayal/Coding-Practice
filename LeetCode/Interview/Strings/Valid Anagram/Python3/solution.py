class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Convert the strings to lists of characters
        s = list(s)
        t = list(t)
        
        # Sort the lists in ascending order
        s.sort()
        t.sort()
        
        # Compare the sorted lists
        return (s == t)
