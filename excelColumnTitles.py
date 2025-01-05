
from itertools import product
from string import ascii_uppercase

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        """
        Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

        For example:

        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28 
        ...
        

        Example 1:

        Input: columnNumber = 1
        Output: "A"
        Example 2:

        Input: columnNumber = 28
        Output: "AB"
        Example 3:

        Input: columnNumber = 701
        Output: "ZY"

        """
        assert 1 <= columnNumber <= 2**31 - 1, f"Column number must be an integer greater than 0 and less or equal to  2^31 - 1"

        xl_titles = []
        for i in range(1, 6):
            #session is crashing after 6
            print(i)
            combs = [''.join(list(item)) for item in product(ascii_uppercase, repeat=i)]
            xl_titles.extend(combs)
        col_title  = xl_titles[columnNumber - 1]

        assert isinstance(col_title, str), "'Return' type is not a string"
        
        return col_title

# len(xl_titles) = 12356630