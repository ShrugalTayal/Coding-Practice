class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Convert x and y to binary strings
        x = bin(x)[2:]
        y = bin(y)[2:]
        
        # Make x and y of equal length by adding leading zeros
        size = max(len(x), len(y))
        x = "0" * (size - len(x)) + x
        y = "0" * (size - len(y)) + y
        
        # Calculate the Hamming distance
        hamd = 0
        for i in range(size):
            if x[i] != y[i]:
                hamd += 1
        
        return hamd
