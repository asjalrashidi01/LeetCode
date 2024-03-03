#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        my_stack = []

        for i in tokens:
            if i == "+":
                my_stack.append(int(my_stack.pop() + my_stack.pop()))
            elif i == "-":
                val1 = my_stack.pop()
                val2 = my_stack.pop()
                my_stack.append(int(val2 - val1))
            elif i == "*":
                my_stack.append(int(my_stack.pop() * my_stack.pop()))
            elif i == "/":
                val1 = my_stack.pop()
                val2 = my_stack.pop()
                my_stack.append(int(val2 / val1))
            else:
                my_stack.append(int(i))

        return my_stack.pop()
        
# @lc code=end

