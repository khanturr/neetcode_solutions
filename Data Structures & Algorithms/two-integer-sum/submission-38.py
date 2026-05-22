class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #nums is an array of integers
    #target is an integer
    #return is the indices i and j such that nums[i] + nums[j] == target and i != j
        my_hashmap = {}
        for i in range(len(nums)):
            if target-nums[i] in my_hashmap:
                return [my_hashmap[target-nums[i]], i]
            else:
                my_hashmap[nums[i]] = i
            
        #O(n^2) time, O(1) space