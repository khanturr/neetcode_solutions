class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}
        for i, n in enumerate(nums):
            if (target - n) in mymap:
                return [mymap[target-n], i]
            mymap[n] = i

