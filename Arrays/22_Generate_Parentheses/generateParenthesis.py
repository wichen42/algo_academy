# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

def generateParentheses(n):
    stack = []
    res = []
    
    def _backtrack(open, close):
        if open == close == n:
            res.append("".join(stack))
            return
        
        if open < n:
            stack.append("(")
            _backtrack(open+1, close)
            stack.pop()
        
        if close < open:
            stack.append(")")
            _backtrack(open, close+1)
            stack.pop()
        
        _backtrack(0,0)
        return res