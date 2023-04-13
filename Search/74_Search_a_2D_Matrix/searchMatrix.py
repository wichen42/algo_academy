# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

def searchMatrix(matrix, target):
    left, right = 0, len(matrix)-1
    count = 0
    
    while left <= right:
        mid = left + (right-left)//2
        
        if target in matrix[mid]:
            return True
        elif matrix[mid][0] > target:
            right = mid-1
        elif matrix[mid][0] < target:
            left = mid+1
        else:
            return False