class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mymap = {}
        for i, n in enumerate(nums):
            if n in mymap: #check if in hashmap
                return True
            mymap[n] = i
        return False 