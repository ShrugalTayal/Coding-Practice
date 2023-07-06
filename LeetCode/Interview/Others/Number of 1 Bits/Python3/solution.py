class Solution:
    def hammingWeight(self, n: int) -> int:
        # Convert the integer to its binary representation and count the number of '1' bits
        return bin(n).count("1")
