#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()

        L = 0
        R = len(s) - 1

        while L < R:
            if not self.isAlphaNum(s[L]):
                L += 1
            elif not self.isAlphaNum(s[R]):
                R -= 1
            elif (s[L] != s[R]):
                return False
            else:
                L += 1
                R -= 1

        return True
    
    def isAlphaNum (self, c):
        if ord(c) <= ord('z') and ord(c) >= ord('a'):
            return True
        elif ord(c) <= ord('9') and ord(c) >= ord('0'):
            return True
        else:
            return False
        
# @lc code=end

