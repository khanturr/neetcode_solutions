class Solution:
    def validPalindrome(self, s: str) -> bool:
        cleaned = "".join(filter(str.isalnum, s)).lower()
        def ispal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return ispal(i + 1, j) or ispal(i, j - 1)
            i += 1
            j -= 1

        return True
            
            
