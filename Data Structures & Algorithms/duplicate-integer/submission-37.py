class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myhash = {}
        for i in range(len(nums)):
            if nums[i] in myhash:
                return True
            else:
                myhash[nums[i]] = i
        return False