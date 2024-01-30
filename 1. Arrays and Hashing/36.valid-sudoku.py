#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        answer = True

        # Checking vertically
                
        for i in range(9):
            num_hash = {}
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] not in num_hash.keys():
                    num_hash[board[i][j]] = 1
                else:
                    return False
                
        # Checking horizontally
                
        for i in range(9):
            num_hash = {}
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif board[j][i] not in num_hash.keys():
                    num_hash[board[j][i]] = 1
                else:
                    return False
                
        # Checking boxes
        
        for i in range(3):
            for j in range(3):
                num_hash = {}
                length = 3*(i+1) - 1
                breadth = 3*(j+1) - 1
                for k in range(length - 2, length+1):
                    for l in range(breadth - 2, breadth+1):
                        if board[k][l] == ".":
                            continue
                        elif board[k][l] not in num_hash.keys():
                            num_hash[board[k][l]] = 1
                        else:
                            return False

        return answer
    
        
# @lc code=end

