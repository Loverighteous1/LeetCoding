"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

 

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1
 

Constraints:

0 <= x, y <= 231 - 1

"""

# Solution

class Solution:
    
    def decimal_to_binary(self, number: int, bit_width=None):
        
        binary_number = ""

        while number > 0:
            binary_number = str(number % 2) + binary_number
            number = number // 2  

            if binary_number:
                binary_number = binary_number 
            else:
                binary_number =  "0"


        if bit_width is not None:
            binary_number = binary_number.zfill(bit_width)

        
    def hammingDistance(self, x: int, y: int) -> int:
        """
        Description: 
            The Hamming distance between two integers is the number of positions at which the 
            corresponding bits are different.

        Args:   Given two integers x and y, 
        Return: 
        ham_dist : hamming_distance between x and y -> interger.

        """
        assert 0 <= x and y <= 2**31 - 1, f" 0 <= x and y <= 2^31 - 1 "
        x_binary = str(self.decimal_to_binary(x,4))
        y_binary = str(self.decimal_to_binary(y,4))
        ham_dist = 0
        for i in range(len(x_binary)):
            if x_binary[i] != y_binary[i]:
                ham_dist += 1 
        return ham_dist