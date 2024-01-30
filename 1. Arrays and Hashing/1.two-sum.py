#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_hash = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen_hash.keys():
                return [seen_hash[diff], i]
            else:
                seen_hash[nums[i]] = i
        
# @lc code=end

