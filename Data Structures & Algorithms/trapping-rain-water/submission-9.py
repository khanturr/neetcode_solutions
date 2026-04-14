class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_height_left = 0
        max_height_right = 0
        total = 0
        while i < j:
            if height[i] <= height[j]:
                if height[i] < max_height_left:
                    current_water = max_height_left - height[i]
                    total += current_water
                else:
                    max_height_left = max(max_height_left, height[i])
                i += 1
            else:
                if height[j] < max_height_right:
                    current_water = max_height_right - height[j]
                    total += current_water
                else:
                    max_height_right = max(max_height_right, height[j])
                j -= 1
        return total
        
        
        