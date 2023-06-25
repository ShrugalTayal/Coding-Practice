class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Convert matrix to 1D list
        matrix1d = []
        
        # Transpose the matrix and append each column to matrix1d
        for i in range(len(matrix)):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            temp.reverse()  # Reverse the column
            matrix1d.extend(temp)  # Append the reversed column to matrix1d
        print(matrix1d)
        
        # Reconstruct the matrix using the modified matrix1d
        index = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                # Assign the elements from matrix1d back to the matrix row by row
                matrix[i][j] = matrix1d[i + j + index]
            index = index + len(matrix) - 1  # Update the index for the next row
        print(matrix)
