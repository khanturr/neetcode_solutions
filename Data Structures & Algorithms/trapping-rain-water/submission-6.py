class Solution:
    def trap(self, height: List[int]) -> int:
        #edge cases
        total = 0
        maxr = 0
        maxl = 0
        for p in range(len(height)):
            maxl = max(height[0:p+1], default=0)
            maxr = max(height[p:], default=0)
            current_water = min(maxl, maxr) - height[p]
            total += current_water
        return total
        
        
        
        