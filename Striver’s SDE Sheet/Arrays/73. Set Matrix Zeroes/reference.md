---

## Set Matrix Zeroes

**Problem Link:** [Set Matrix Zeroes - LeetCode](https://leetcode.com/problems/set-matrix-zeroes/description/)

**Problem Description:**

Given an `m x n` matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

**Example 1:**

![Example 1](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)

```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

**Example 2:**

![Example 2](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)

```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

**Constraints:**

- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`

**Approach:**

One approach to solve this problem in-place is to use the first row and first column of the matrix to store information about the zeros. We can traverse the matrix, and if we encounter a zero at position `(i, j)`, we can set the value at `matrix[0][j]` and `matrix[i][0]` to zero. This way, the first row and first column act as indicators for the respective rows and columns that need to be zeroed out.

To handle the first row and first column separately, we can use two Boolean variables `firstRowZero` and `firstColZero`. These variables will store whether the first row or first column needs to be zeroed out. After traversing the matrix, we can update the matrix by setting the rows and columns indicated by the first row and first column to zeros.

1. Initialize `firstRowZero` and `firstColZero` as `False`.
2. Traverse the matrix from top to bottom and left to right.
   - If `matrix[i][j]` is zero, set `matrix[0][j]` and `matrix[i][0]` to zero.
   - If `i == 0`, set `firstRowZero` to `True`.
   - If `j == 0`, set `firstColZero` to `True`.
3. Traverse the matrix again, starting from `(1, 1)` position.
   - If `matrix[i][j]` is zero, set the entire row `matrix[i]` to zeros.
   - If `matrix[i][j]` is zero, set the entire column `matrix[:, j]` to zeros.
4. If `firstRowZero` is `True`, set the entire first row `matrix[0]` to zeros.
5. If `firstColZero` is `True`, set the entire first column `matrix[:, 0]` to zeros.

**Complexity Analysis:**

The time complexity for this approach is O(m \* n), where m is the number of rows and n is the number of columns in the matrix. We traverse the matrix twice.

The space complexity is O(1) since we are using the first row and first column of the matrix to store information about the zeros.

**Reference Implementation:**

Python:
```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        firstRowZero = False
        firstColZero = False

        # Check if first row or first column needs to be zeroed out
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        firstRowZero = True
                    if j == 0:
                        firstColZero = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set rows and columns indicated by the first row and first column to zeros
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Set the entire first row to zeros if indicated by firstRowZero
        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0

        # Set the entire first column to zeros if indicated by firstColZero
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0
```

Java:
```java
class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        boolean firstRowZero = false;
        boolean firstColZero = false;

        // Check if first row or first column needs to be zeroed out
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    if (i == 0)
                        firstRowZero = true;
                    if (j == 0)
                        firstColZero = true;
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        // Set rows and columns indicated by the first row and first column to zeros
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;
            }
        }

        // Set the entire first row to zeros if indicated by firstRowZero
        if (firstRowZero) {
            for (int j = 0; j < n; j++) {
                matrix[0][j] = 0;
            }
        }

        // Set the entire first column to zeros if indicated by firstColZero
        if (firstColZero) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }
    }
}
```

---
