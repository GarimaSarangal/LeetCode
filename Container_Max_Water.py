class Solution:
    def maxArea(self, height: List[int]) -> int:
    #https://leetcode.com/problems/container-with-most-water/
        i = 0
        j = len(height)-1
        max_vol = 0
        
        while i < j:
            if height[j] > height[i]:
                max_vol = max(max_vol, height[i] * (j-i))
                i += 1
            else:
                max_vol = max(max_vol, height[j] * (j-i))
                j -= 1
            
            
        return max_vol
