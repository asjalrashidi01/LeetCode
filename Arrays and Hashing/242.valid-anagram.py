#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        for i in s:
            if i not in s_hash.keys():
                s_hash[i] = 1
            else:
                s_hash[i] += 1

        t_hash = {}
        for i in t:
            if i not in t_hash.keys():
                t_hash[i] = 1
            else:
                t_hash[i] += 1

        if s_hash == t_hash:
            return True
        else:
            return False
        
# @lc code=end

