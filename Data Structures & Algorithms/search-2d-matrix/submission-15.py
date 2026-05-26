class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for me in matrix:
            l = 0
            r = len(me) - 1
            while l <= r:
                m = (l+r) // 2
                if me[m] > target:
                    r = m - 1
                elif me[m] < target:
                    l = m + 1
                else:
                    return True
        return False
            
            