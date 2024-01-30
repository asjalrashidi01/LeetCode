#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_hash = defaultdict(list)

        for i in strs:
            count_hash = [0] * 26
        
            for j in i:
                count_hash[ord(j) - ord("a")] += 1

            anagram_hash[tuple(count_hash)].append(i)

        return anagram_hash.values()
        
        
# @lc code=end

