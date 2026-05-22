class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #nums is an array of integers
    #target is an integer
    #return is the indices i and j such that nums[i] + nums[j] == target and i != j
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target and i!=j:
                    return [i, j]
        return False