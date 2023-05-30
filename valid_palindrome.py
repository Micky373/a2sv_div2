class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean_string = ''

        for string in s.lower():
            if string.isalnum():
                clean_string+=string

        new_string = clean_string[::-1]

        return new_string == clean_string