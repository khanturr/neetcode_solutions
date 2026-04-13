class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = [i for i in set(nums)]
        print(dups)
        return len(nums) != len(dups)
