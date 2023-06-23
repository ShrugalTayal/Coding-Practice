class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Convert the list of digits to a string representation
        val = str(digits)[1:-1]
        
        # Split the string by comma and space to get individual digits
        val = val.split(", ")
        
        # Join the digits to form a single string
        val = "".join(val)
        
        # Convert the string to an integer, increment it by 1, and convert it back to a string
        val = str(int(val) + 1)
        
        # Convert the string back to a list of integers
        digits = list(val)
        
        # Convert each element in the list from string to integer
        for i in range(len(digits)):
            digits[i] = int(digits[i])
        
        return digits
