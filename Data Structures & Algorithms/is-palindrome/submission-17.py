class Solution:
    def isPalindrome(self, s: str) -> bool:
        w = s[::-1]
        result1 = "".join(char for char in w if char.isalnum()).lower()
        result2 = "".join(char for char in s if char.isalnum()).lower()
        if result1 == result2:
            return True
        return False