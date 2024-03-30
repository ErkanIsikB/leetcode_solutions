# Given
# an
# array
# of
# integers
# nums
# which is sorted in ascending
# order, and an
# integer
# target, write
# a
# function
# to
# search
# target in nums.If
# target
# exists, then
# return its
# index.Otherwise,
# return -1.
#
# You
# must
# write
# an
# algorithm
# with O(log n) runtime complexity.
#
# Example
# 1:
#
# Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
# Output: 4
# Explanation: 9
# exists in nums and its
# index is 4
# Example
# 2:
#
# Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
# Output: -1
# Explanation: 2
# does
# not exist in nums
# so
# return -1
#
# Constraints:
#
# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All
# the
# integers in nums
# are
# unique.
# nums is sorted in ascending
# order.
nums = [-1, 0, 3, 5, 9, 12]
target = 2
def search():
    try:
        return nums.index(target)
    except:
        return -1

def search_2():
    i, j = 0, len(nums) - 1
    while i <= j:
        if nums[(i + j) // 2] == target:
            return (i + j) // 2
        elif nums[(i + j) // 2] < target:
            i = 1 + (i + j) // 2
        else:
            j = -1 + (i + j) // 2
    return -1


print(search_2())