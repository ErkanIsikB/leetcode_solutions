# Given
# an
# integer
# array
# nums,
# return an
# array
# answer
# such
# that
# answer[i] is equal
# to
# the
# product
# of
# all
# the
# elements
# of
# nums except nums[i].
#
# The
# product
# of
# any
# prefix or suffix
# of
# nums is guaranteed
# to
# fit in a
# 32 - bit
# integer.
#
# You
# must
# write
# an
# algorithm
# that
# runs in O(n)
# time and without
# using
# the
# division
# operation.
#
# Example
# 1:
#
# Input: nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]
# Example
# 2:
#
# Input: nums = [-1, 1, 0, -3, 3]
# Output: [0, 0, 9, 0, 0]

nums = [-1, 1, 0, -3, 3]
def productExceptSelf():
    length = len(nums)
    products = [1] * length
    for i in range(1, length):
        products[i] = products[i - 1] * nums[i - 1]

    right = nums[-1]
    for i in range(length - 2, -1, -1):
        products[i] *= right
        right *= nums[i]

    return products

print(productExceptSelf())
