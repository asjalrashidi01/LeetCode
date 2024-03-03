#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n >= 1:
            n1 = 0
            n2 = 1

            for i in range(n-2):
                new_n1 = n2
                new_n2 = n1+n2

                n1 = new_n1
                n2 = new_n2
            
            return n1+n2
        
# @lc code=end

