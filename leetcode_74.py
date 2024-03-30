# You
# are
# given
# an
# m
# x
# n
# integer
# matrix
# matrix
# with the following two properties:
#
# Each
# row is sorted in non - decreasing
# order.
# The
# first
# integer
# of
# each
# row is greater
# than
# the
# last
# integer
# of
# the
# previous
# row.
# Given
# an
# integer
# target,
# return true if target is in matrix or false
# otherwise.
#
# You
# must
# write
# a
# solution in O(log(m * n))
# time
# complexity.
#
# Example
# 1:
#
# Input: matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 3
# Output: true
# Example
# 2:
#
# Input: matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 13
# Output: false
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
def searchMatrix():
    i = 0
    while i < len(matrix):
        j = len(matrix[i]) - 1
        if matrix[i][j] < target:
            i += 1
        else:
            if target in matrix[i]:
                return True
            else:
                return False
    return False
print(searchMatrix())