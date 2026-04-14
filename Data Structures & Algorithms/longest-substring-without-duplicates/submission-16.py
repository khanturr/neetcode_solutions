class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_value = 0
        for i in range(len(s)):
            sub = [s[i]]
            max_value = max(max_value, 1)
            for j in range(i+1, len(s)):
                if s[j] not in sub:
                    sub.append(s[j])
                    max_value = max(max_value, len(sub))
                else:
                    break
        return max_value