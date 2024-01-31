#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:

        max = 0

        L, R = 0, len(height) - 1

        while (L < R):
            area = (R-L) * (min(height[L], height[R]))
            if area > max:
                max = area
            else:
                if height[L] > height[R]:
                    R -= 1
                else:
                    L += 1

        return max
        
# @lc code=end

