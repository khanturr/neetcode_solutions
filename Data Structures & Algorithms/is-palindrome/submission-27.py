class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        t = s[::-1]
        return s == t
