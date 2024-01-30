#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []

        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            L, R = i+1, len(nums) - 1

            while (L < R):
                threesum = nums[i] + nums[L] + nums[R]
                if threesum == 0:
                    answer.append([nums[i], nums[L], nums[R]])
                    L += 1
                    while (nums[L] == nums[L-1] and L < R):
                        L += 1
                elif threesum > 0:
                    R -= 1
                elif threesum < 0:
                    L += 1
        
        return answer


# @lc code=end

