class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for dup in range(len(nums)):
            for m in range(dup+1, len(nums)):
                if nums[dup] == nums[m]:
                    return True           
        return False