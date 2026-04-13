class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            new = ''.join(sorted(s))
            print(new)
            res[new].append(s)
        return list(res.values())
