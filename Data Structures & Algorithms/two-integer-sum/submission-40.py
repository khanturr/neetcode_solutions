class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #declare hashmap
        my_hashmap = {}
        #iterate thru loop
        for i in range(len(nums)):
            if target-nums[i] in my_hashmap:
                return [my_hashmap[target-nums[i]], i]
            else:
                my_hashmap[nums[i]] = i
        return True

