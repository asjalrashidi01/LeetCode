#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0: return 0

        numSet = set(nums)

        answer = 0

        num = numSet.pop()

        count = 1

        while numSet:
            temp = num

            while (num+1) in numSet:
                count += 1
                numSet.remove(num + 1)
                num = num + 1

            num = temp

            while (num - 1) in numSet:
                count += 1
                numSet.remove(num - 1)
                num = num - 1

            answer = max(answer, count)

            if not numSet:
                break

            num = numSet.pop()

            count = 1

        return max(answer, count)



        
            
        
# @lc code=end

