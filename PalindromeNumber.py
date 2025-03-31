class Solution(object):
    def isPalindrome(self, x):
        converted_integer = str(x)
        reversed_integer = converted_integer[::-1]

        return converted_integer == reversed_integer
