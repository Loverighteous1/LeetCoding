from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        """
        Description:
        You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. 
        Each integer appears exactly once except a which appears twice and b which is missing. The task 
        is to find the repeating and missing numbers a and b.

        Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.
        
        Input: a 2D matrix of size n * n where elements are in range [1, n*n]

        Output: a 1D array of size 2 where elements are respectively repeated and 
        missing in the 2D matrix
        
        """
        n = len(grid[0])
        assert 2 <= n <= 50, "Grid size n must be between 2 and 50."
            
        ll = []
        for row in grid:
            assert len(row) == n, "All rows in the grid must have the same length as n."
            ll.extend(row)
        
        max_value = n * n
        for value in ll:
            assert 1 <= value <= max_value, f"All values in the grid must be between 1 and {max_value}."
        
        
        unique_values = set(ll)
        missing_value_count = 0
        for x in range(1, max_value + 1):
            if x not in unique_values:
                missing_value_count += 1
        assert missing_value_count == 1, "There must be exactly one value between 1 and n*n that is missing from the grid."

        repeated_value_count = 0
        for x in range(1, max_value + 1):
            if ll.count(x) == 2:
                repeated_value_count += 1
        assert repeated_value_count == 1, "There must be exactly one value between 1 and n*n that appears exactly twice in the grid."

        unique_value_count = 0
        for x in range(1, max_value + 1):
            if ll.count(x) == 1:
                unique_value_count += 1
        assert unique_value_count == max_value - 2, "All values except two must appear exactly once in the grid."

        
        ll = sorted(ll)
        ans = []

        for i in range(0, n-1):
            if ll[i] == ll[i+1]:
                ans.append(ll[i])


        for i in range(1, n+1):
            if i not in ll:
                ans.append(i)



### Test cases

sol = Solution()
grid = [[1, 3], [2, 2]]
sol.findMissingAndRepeatedValues(grid)
print(grid) # output [2, 4]

grid = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
sol.findMissingAndRepeatedValues(grid)
print(grid) # output [9, 5]


grid = [[1, 1], [2, 3]]
sol.findMissingAndRepeatedValues(grid)
print(grid) # output [1, 4]

grid = [[1], [2], [3], [3]]
sol.findMissingAndRepeatedValues(grid)
print(grid) # output [3, 4]

grid = [[1]]  
sol.findMissingAndRepeatedValues(grid)
print(grid) # output AssertionError: Grid size n must be between 2 and 50.

grid = [[1, 2], [3]]
sol.findMissingAndRepeatedValues(grid)
print(grid) # output AssertionError: All rows in the grid must have the same length as n.

grid = [[1, 2], [3, 100]]
sol.findMissingAndRepeatedValues(grid)
print(grid) # output AssertionError: All values in the grid must be between 1 and 4.

grid = [[1, 2], [3, 3]]
sol.findMissingAndRepeatedValues(grid)
print(grid) # output AssertionError: There must be exactly one value between 1 and n*n that is missing from the grid.


grid = [[1, 2], [3, 4]]
sol.findMissingAndRepeatedValues(grid)
print(grid) # output AssertionError: There must be exactly one value between 1 and n*n that appears exactly twice in the grid.


grid = [[1, 1], [2, 2]]
sol.findMissingAndRepeatedValues(grid)
print(grid) # output AssertionError: All values except two must appear exactly once in the grid.


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
sol.findMissingAndRepeatedValues(grid)
print(grid) # output AssertionError: There must be exactly one value between 1 and n*n that is missing from the grid.