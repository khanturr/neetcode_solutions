class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mymap = {}
        
        for i, n in enumerate(nums):
            if n in mymap and abs(i - mymap[n]) <= k:
                return True
            mymap[n] = i
        
        return False