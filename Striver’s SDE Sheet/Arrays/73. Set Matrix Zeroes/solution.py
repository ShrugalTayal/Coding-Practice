class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        columns = []
        
        # Identify the columns that need to be zeroed out
        for i in range(len(matrix)):
            if 0 in matrix[i]:
                count = matrix[i].count(0)
                row = list(matrix[i])
                for j in range(count):
                    index = row.index(0)
                    columns.append(index)
                    row[index] = None

        # Set the rows indicated by columns to zeros
        for i in range(len(matrix)):
            if 0 in matrix[i]:
                matrix[i] = [0]*len(matrix[i])

        # Set the columns indicated by columns to zeros
        for i in range(len(matrix)):
            for j in columns:
                matrix[i][j] = 0

        return matrix
