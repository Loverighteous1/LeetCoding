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
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Description:  
        In Pascal's triangle, each number is the sum of the two numbers directly above it.

        Input:  numRows -> an integer
        Return: The first numRows of Pascal's triangle.
        """
        
        # Constraint check
        assert 1 <= numRows <= 30, f"Integer must be in [1, 30]"

        output = [[1], [1,1]]

        if numRows == 1:
            print(list(output[0]))
        elif numRows == 2:
            print(output)
        else:
            for i in range(1, numRows-1):
                previous_l = output[i]
                len_l = len(previous_l)
                newlist = [1]
                for j in range(1, len_l):
                    #print(j)
                    newlist.append(previous_l[j] + previous_l[j-1])
                newlist.append(1)
                #print(newlist)
                output.append(newlist)
            print(output)
            
            #Other form of printing

            # for i in range(len(output)):
            #     print(output[i],'\n')

solution = Solution()
solution.generate(5)