class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)  # Convert the integer to binary representation
        n = n[2:]  # Remove the '0b' prefix from the binary string
        n = '0' * (32 - len(n)) + n  # Pad the binary string with leading zeros to make it 32 bits long
        n = n[::-1]  # Reverse the binary string
        n = int(n, 2)  # Convert the reversed binary string back to an integer
        
        return n
