class Solution:
    def isPalindrome(self, s: str) -> bool:

        res = ''.join(filter(lambda char: char.isalnum(), s)).lower()

        return res == res[::-1]
        