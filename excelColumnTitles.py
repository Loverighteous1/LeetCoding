from string import ascii_uppercase

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        """
        Description:
        Given an integer columnNumber, the function returns its corresponding column title as it appears in an Excel sheet.

        Inputs: 
            columnNumber : an integer between 1 and 2^31 - 1

        Outputs:
            title: string of character(s) as in excel sheets

        """
        assert 1 <= columnNumber <= 2**31 - 1, f"{columnNumber} must be an integer in [1,  {2**31 - 1}]"
        alphabet = string.ascii_uppercase
        user_colnb = columnNumber - 1
        if user_colnb < 26:
            col_title = alphabet[user_colnb]
            assert 1<= len(col_title) <= 7, "The title length is not in [1, 7]"
            # assert "A" <= col_title <= "FXSHRXW", f"{col_title} is not in [A, FXSHRXW]"
            return col_title
        quotient = user_colnb//26
        remainder = user_colnb%26
        col_title = convertToTitle(quotient) + alphabet[remainder]
        assert isinstance(col_title, str), "'Return' type is not a string"
        assert 1<= len(col_title) <= 7, "The title length is not in [1, 7]"
        return col_title
        


"""
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