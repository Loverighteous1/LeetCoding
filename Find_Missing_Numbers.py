from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Description:
        Given an array nums of n integers where nums[i] is in the range [1, n], 
        return an array of all the integers in the range [1, n] that do not appear in nums.

        Input:
            nums: a list of n integers where nums[i] is in the range [1, n]

        Output:
            not_in_nums: array of all missing number in nums           
        
        """

        n = len(nums)   
        assert 1 <= n <= 10**5, f'{n} must be in range [1, {10**5}]'
        for x in nums:
            assert isinstance(x, int) and (1 <= x <= n), f"The element {x} must be an integer in [1, {n}]."
        not_in_nums = []
        for i in range(1,n+1):
            if i not in nums:
                not_in_nums.append(i)
        return not_in_nums

#### Tests
sol = Solution()
nums = [4,3,2,7,8,2,3,1]
output = sol.findDisappearedNumbers(nums)
print(f"Missing numbers in {nums} are: {output}") # [5,6]

nums = [1,1]
output = sol.findDisappearedNumbers(nums)
print(f"Missing numbers in {nums} are: {output}") # [2]


nums = [2,1]
output = sol.findDisappearedNumbers(nums)
print(f"Missing numbers in {nums} are: {output}") # []


nums = [2]
output = sol.findDisappearedNumbers(nums)
print(f"Missing numbers in {nums} are: {output}") #AssertionError: 2 must be an integer in [1, 1].


nums = [1, "hello"]
output = sol.findDisappearedNumbers(nums)
print(f"Missing numbers in {nums} are: {output}") #AssertionError: The element hello must be an integer in [1, 2].