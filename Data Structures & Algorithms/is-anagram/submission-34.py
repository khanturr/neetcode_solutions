class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        mymap = {}
        mymap1 = {}
        for i in range(len(s)):
            mymap[s[i]] = 1 + mymap.get(s[i], 0)
            mymap1[t[i]] = 1 + mymap1.get(t[i], 0)
        return mymap == mymap1

