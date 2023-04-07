# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

def isValid(str):
    
    closetoOpen = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }

    stack = []
    
    # str = (())
    
    for open in str:
        if open in closetoOpen:
            if stack and stack[-1] == closetoOpen[open]:
                stack.pop()
            else:
                return False
        else:
            stack.append(open)
            
    return True if not stack else False

print(isValid("()"))