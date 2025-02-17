"""

2    4    -1            2    -10    18
-10  5    11    ====>   4      5    -7
18   -7    6           -1     11     6

 

Example 1:

Input: 

Example 2:

Input: matrix = 
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105

"""
from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Description:
            Given a 2D integer array matrix, return the transpose of matrix.
            The transpose of a matrix is the matrix flipped over its main diagonal, 
            switching the matrix's row and column indices.

        Input:
        matrix : list of m lists (rows) of n elements each (columns) 

        Output:
        Transpose of a matrix of n rows and m columns

        """

        assert isinstance(matrix, List), "Your input must be a list"
        m = len(matrix)
        n = len(matrix[0])

        for row in matrix:
            assert isinstance(row, List), "Each row must be a list"
            assert n == len(row), f"  Number of elements in {row} must be {n} "
            for k in range(n):
                assert isinstance(row[k], int), f" {row[k]} in {row} must be an integer"
            

        assert 1<= m <= 1000 and 1<= n <= 1000 and 1<= m * n <= 105, "Number of rows and columns must be in [1,1000] and their product in [1,105]"
        
        transpose_mat = []

        for i in range(n):
            trans_row = []
            for row in matrix:
                trans_row.append(row[i])
            transpose_mat.append(trans_row)
            
        return transpose_mat


### test cases

transpose_matrix = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
transpose_matrix.transpose(matrix)
print(transpose_matrix) # Output: [[1,4,7],[2,5,8],[3,6,9]]

matrix1 = [[1,2,3],[4,5,6]]
transpose_matrix.transpose(matrix1)
print(transpose_matrix) # Output: [[1,4],[2,5],[3,6]]

matrix2 = [
    [3, 5],
    [1, 8],
    [6, 4],
    [0, 0, 0]
]
transpose_matrix.transpose(matrix2)
print(transpose_matrix) # AssertionError:   Number of elements in [0, 0, 0] must be 2 

matrix3 = [
    [3, 5],
    [1, 8],
    [6, [4]]
]

transpose_matrix.transpose(matrix3)
print(transpose_matrix) # AssertionError:  [4] in [6, [4]] must be an integer

