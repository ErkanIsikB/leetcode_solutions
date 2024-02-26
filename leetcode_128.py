# Given
# an
# unsorted
# array
# of
# integers
# nums,
# return the
# length
# of
# the
# longest
# consecutive
# elements
# sequence.
#
# You
# must
# write
# an
# algorithm
# that
# runs in O(n)
# time.
#
# Example
# 1:
#
# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The
# longest
# consecutive
# elements
# sequence is [1, 2, 3, 4].Therefore
# its
# length is 4.
# Example
# 2:
#
# Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# Output: 9

nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
def longestConsecutive():
    sorte = sorted(set(nums))
    k = 1
    lengths = {}
    if nums == []:
        return 0
    for i in range(len(sorte) - 1):
        if sorte[i] == sorte[i + 1] - 1:
            k += 1
        else:
            lengths[i] = k
            k = 1
    lengths[-1] = k
    maxkey = max(lengths, key=lengths.get)
    return lengths[maxkey]

print(longestConsecutive())