class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #for each str in strs, compare each pair and see whether they are anagrams
        #if they are an anagram, add them to a sublist (key/value)
        #then print values
        myhashmap = defaultdict(list)
        for s in strs:
            sorteda = ''.join(sorted(s))
            myhashmap[sorteda].append(s)
        
        return list(myhashmap.values())
        

