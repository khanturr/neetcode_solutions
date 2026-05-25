class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #numbers is an array of inegers that is sorted increasingly
        #1-indexed
        #return nums[i] + nums[j] = target and i < j, i!=j
        for i in range(len(numbers)):
            for j in range(i, len(numbers)):
                if numbers[i] + numbers[j] == target and i < j:
                    return [i+1,j+1]
        