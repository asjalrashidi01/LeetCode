#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:

        my_stack = []

        for c in s:
            if c == '(' or c == '[' or c == "{":
                my_stack.append(c)
            elif c == ')':
                if my_stack == [] or my_stack.pop(-1) != '(':
                    return False
            elif c == ']':
                if my_stack == [] or my_stack.pop(-1) != '[':
                    return False
            elif c == '}':
                if my_stack == [] or my_stack.pop(-1) != '{':
                    return False
                
        if my_stack == []:
            return True
        else:
            return False
        
# @lc code=end

