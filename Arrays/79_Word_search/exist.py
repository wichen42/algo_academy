# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

def exist(board, word):
    # base cases
    #   1. if we find the word, return True
    #       a. keep track of index. done when i == len(word)
    #   2. False
    #       a. out of bounds
    #       b. letter does not match with word[i]
    #       c. we have visited
    
    rows, cols = len(board), len(board[0])
    visited = set()
    
    def _backtrack(r, c, i):
        if i == len(word):
            return True
        
        if not _inbound(r,c) or word[i] != board[r][c] or (r,c) in visited:
            return False
        
        # modify
        visited.add((r,c))
        
        # recursion
        res = _backtrack(r+1, c, i+1) or _backtrack(r-1, c, i+1) or _backtrack(r, c+1, i+1) or _backtrack(r, c-1, i+1)
        
        # backtrack
        visited.discard((r,c))
        
    def _inbound(r, c):
        rowInbound = r >= 0 and r < rows
        colInbound = c >= 0 and c < cols
        
        return rowInbound and colInbound
    
    for r in range(rows):
        for c in range(cols):
            if _backtrack(r, c, 0):
                return True
            
    return False