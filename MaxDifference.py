
class Solution:
    def maxDifference(self, s: str) -> int:
        """
        Description:
            Given a string s consisting of lowercase English letters. 
            Your task is to find the maximum difference between the frequency of
            two characters in the string such that:

            One of the characters has an even frequency in the string.
            The other character has an odd frequency in the string.
            Return the maximum difference, calculated as the frequency of the 
            character with an odd frequency minus the frequency of the character
            with an even frequency.
        
            Input:
                s: string
            
            Output:
                Return the difference between the ood max and the even max
        """
        assert 3<= len(s) <= 100
        assert all(low.islower() for low in s), "Each character in the string should be a lowercase"
        odd_occurrence = []
        even_occurrence = []
        uniq_car = list(set(s))
        for car in uniq_car:
            occur = s.count(car)
            if occur%2 == 0:
                even_occurrence.append(occur)
            else:
                odd_occurrence.append(occur)

        assert len(even_occurrence) != 0, "String does not contain any even frequency"
        assert len(odd_occurrence) != 0, "String does not contain any odd frequency"
        
        return max(odd_occurrence) - max(even_occurrence)


#Cases test
sol = Solution()
s = "abcabcab"
output = sol.maxDifference(s) 
print(output)# output 1

s = "aaaaabbc"
output = sol.maxDifference(s) 
print(output)# output 3

s = "abaDab"
output = sol.maxDifference(s) 
print(output)# AssertionError: Each character in the string should be a lowercase

s = "aba"
output = sol.maxDifference(s) 
print(output)# output -1

s = "helo"
output = sol.maxDifference(s) 
print(output)# AssertionError: String does not contain any even frequency

s = "he"
output = sol.maxDifference(s) 
print(output) #AssertionError: String must be at least of length 3 and at most 100
        