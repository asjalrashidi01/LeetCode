#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        len_list = len(nums)
        len_unique = len(set(nums))

        return len_list != len_unique
        
        
# @lc code=end

