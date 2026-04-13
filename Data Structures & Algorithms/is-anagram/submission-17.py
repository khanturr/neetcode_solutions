class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        mymaps = {}
        mymapt = {}

        for i in range(len(s)):
            mymaps[s[i]] = 1 + mymaps.get(s[i], 0)
            mymapt[t[i]] = 1 + mymapt.get(t[i], 0)
        return mymaps == mymapt