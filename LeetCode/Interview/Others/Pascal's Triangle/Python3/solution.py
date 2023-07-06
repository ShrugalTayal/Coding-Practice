class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        matrix = []
        
        # Iterate through each row
        for i in range(numRows):
            # Create a new row and fill it with 1's
            matrix.append([1] * (i + 1))
            
        # Generate the values for the remaining rows
        for i in range(2, numRows):
            for j in range(1, i):
                # Calculate the value by summing the two numbers directly above
                matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j]
        
        return matrix
