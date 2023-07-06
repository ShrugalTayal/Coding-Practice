class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)  # Convert the integer to binary representation
        n = n[2:]  # Remove the '0b' prefix from the binary string
        n = '0' * (32 - len(n)) + n  # Pad the binary string with leading zeros to make it 32 bits long
        sum = 0  # Initialize a variable to hold the reversed number
        
        # Iterate through the binary string from left to right
        for i in range(len(n)):
            if n[i] == '1':  # Check if the current bit is 1
                sum = sum + 2 ** i  # Update the sum by adding 2 raised to the power of the current index
        
        return int(sum)  # Convert the sum back to an integer and return it
