#
# @lc app=leetcode id=2733 lang=python3
#
# [2733] Neither Minimum nor Maximum
#

# @lc code=start
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:

        min = nums[0]
        max = nums[0]

        for i in nums:
            if i > max:
                max = i
            if i < min:
                min = i
        
        for i in nums:
            if i != max and i != min:
                return i
        
        return -1
        
# @lc code=end

