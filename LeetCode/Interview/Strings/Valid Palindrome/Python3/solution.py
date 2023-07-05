class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert string to lowercase
        s = s.lower()

        # Remove non-alphanumeric characters and create a temporary string
        temp = ""
        for i in s:
            if i.isalnum():
                temp = temp + i

        # Convert the temporary string and its reverse into lists
        s = list(temp)
        rev = list(temp)

        # Delete the temporary string to free up memory
        del temp

        # Reverse the 'rev' list in-place
        rev.reverse()

        # Print the original and reversed lists (for debugging purposes)
        print(s, rev)

        # Check if the original and reversed lists are equal
        return (s == rev)
