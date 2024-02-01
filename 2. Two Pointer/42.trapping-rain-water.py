#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:

        water = 0

        if len(height) == 0:
            return water

        L, R = 0, len(height) - 1

        max_l, max_r = height[L], height[R]

        while L < R:

            if max_l < max_r:
                L += 1
                max_l = max(max_l, height[L])
                water += max_l - height[L]
            else:
                R -= 1
                max_r = max(max_r, height[R])
                water += max_r - height[R]    

        return water

            
        
        
# @lc code=end

