class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #for each word, check if anagram to other
        new_list = collections.defaultdict(list)
        for words in strs:
            key = "".join(sorted(words))
            new_list[key].append(words)
        return list(new_list.values())