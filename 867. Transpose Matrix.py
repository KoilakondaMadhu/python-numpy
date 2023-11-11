import numpy as np

class Solution:
    def transpose(self, A):
        # Convert the input matrix A to a NumPy array
        nparr = np.array(A)
        
        # Transpose the NumPy array
        nparr = np.transpose(nparr)
        
        # Convert the transposed NumPy array back to a list
        transposed_list = nparr.tolist()
        
        # Return the transposed list
        return transposed_list

# given a 2D integer array matrix, return the transpose of matrix.

# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.


# https://leetcode.com/problems/design-graph-with-shortest-path-calculator/description/?envType=daily-question&envId=2023-11-11

# Case 1
# Case 2
# Input
# matrix =
# [[1,2,3],[4,5,6],[7,8,9]]
# Output
# [[1,4,7],[2,5,8],[3,6,9]]
# Expected
# [[1,4,7],[2,5,8],[3,6,9]]


# ===============================
 

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# Example 2:

# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
 
