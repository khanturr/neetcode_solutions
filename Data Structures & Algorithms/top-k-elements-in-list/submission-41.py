class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #for each element i want to add the frequency as a value, int as key, 
        #then we sort by frequency, get the top k
        mymap = {}
        for n in nums:
            mymap[n] = mymap.get(n, 0) + 1
        top_keys = sorted(mymap, key=mymap.get, reverse=True)
        return top_keys[:k]
        