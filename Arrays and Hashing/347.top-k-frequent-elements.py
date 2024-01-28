#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                
        count_hash = {} # key: number, value: count

        nums_hash = [[] for i in range(len(nums)+1)] # 

        for i in nums:
            count_hash[i] = 1 + count_hash.get(i, 0)

        for i, j in count_hash.items():
            nums_hash[j].append(i)

        answer = []

        for i in range(len(nums_hash) - 1, 0, -1):
            for j in nums_hash[i]:
                answer.append(j)
                if len(answer) == k:
                    return answer
       
        
# @lc code=end

