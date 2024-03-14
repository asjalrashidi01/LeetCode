#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def genPar(n_total: int,  curr_str: string, n_open: int, n_close: int):
            if (len(curr_str) == 2 * n_total):
                res.append(curr_str)
            elif (n_open < n_total and n_close < n_open):
                genPar(n_total, curr_str+"(", n_open+1, n_close)
                genPar(n_total, curr_str+")", n_open, n_close+1)
            elif (n_close < n_open):
                genPar(n_total, curr_str+")", n_open, n_close+1)
            elif (n_open < n_total):
                genPar(n_total, curr_str+"(", n_open+1, n_close)
                

        res = []
        genPar(n, "", 0, 0)

        return res
        
# @lc code=end

