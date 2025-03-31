from typing import List



class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        """
        Description: 
            Given an integer array nums containing positive integers.
            We define a function encrypt such that encrypt(x) replaces every
            digit in x with the largest digit in x. For example, encrypt(523) = 555 
            and encrypt(213) = 333.
            Return the sum of encrypted elements.

        Input: 
        nums: integer array

        Output:
        An integer
        
        
        """
        length = len(nums)
        assert 1 <= length <= 50, "Array length out of range [1,50]"
        for i in range(length):
            assert 1 <= nums[i] <= 1000, f"{nums[i]} is out of range [1,1000]"
            nums[i] = str(nums[i])

        for n in range(length):
            max_dig = str(max([int(dig) for dig in nums[n]])) 
            n_replace = max_dig
            if len(nums[n]) == 1:
                nums[n] = int(n_replace)
            else:
                for nn in range(len(nums[n]) - 1):
                    n_replace += max_dig
                nums[n] = int(n_replace)

        sum_encr = sum(nums)
        
        return sum_encr


###Test cases
sol = Solution()
nums = [1, 2, 3]
result = sol.sumOfEncryptedInt(nums)
print(result) # output 6


nums = [10,21,31]
result = sol.sumOfEncryptedInt(nums)
print(result) #output 66

nums = []
result = sol.sumOfEncryptedInt(nums)
print(result) # Output AssertionError: Array length is out of range [1,50]


nums = []
result = sol.sumOfEncryptedInt(nums)
print(result)  #output  AssertionError: -1 is out of range [1,1000]