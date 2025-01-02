""" 
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:
1 <= numRows <= 30
 
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Description:  
        In Pascal's triangle, each number is the sum of the two numbers directly above it.

        Input:  numRows -> an integer
        Return: The first numRows of Pascal's triangle.
        """