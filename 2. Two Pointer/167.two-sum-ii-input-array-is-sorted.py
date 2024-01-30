#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L , R = 0, len(numbers) - 1

        while L < R:
            sum = numbers[L] + numbers[R]
            if sum == target:
                return [L+1, R+1]
            elif sum > target:
                R -= 1
            elif sum < target:
                L += 1
                
        
# @lc code=end

