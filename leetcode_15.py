# Given
# an
# integer
# array
# nums,
# return all
# the
# triplets[nums[i], nums[j], nums[k]]
# such
# that
# i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice
# that
# the
# solution
# set
# must
# not contain
# duplicate
# triplets.
#
# Example
# 1:
#
# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The
# distinct
# triplets
# are[-1, 0, 1] and [-1, -1, 2].
# Notice
# that
# the
# order
# of
# the
# output and the
# order
# of
# the
# triplets
# does
# not matter.
# Example
# 2:
#
# Input: nums = [0, 1, 1]
# Output: []
# Explanation: The
# only
# possible
# triplet
# does
# not sum
# up
# to
# 0.
# Example
# 3:
#
# Input: nums = [0, 0, 0]
# Output: [[0, 0, 0]]
# Explanation: The
# only
# possible
# triplet
# sums
# up
# to
#
nums = [-1, 0, 1, 2, -1, -4]
def threeSum():
    nums.sort()
    result = []
    for left in range(len(nums) - 2):
        if left > 0 and nums[left] == nums[left - 1]:
            continue
        mid = left + 1
        right = len(nums) - 1

        while mid < right:
            summ = nums[left] + nums[mid] + nums[right]
            if summ < 0:
                mid += 1
            elif summ > 0:
                right -= 1
            else:
                result.append([nums[left], nums[mid], nums[right]])
                while mid < right and nums[mid] == nums[mid + 1]:
                    mid += 1
                while mid < right and nums[right] == nums[right - 1]:
                    right -= 1

                mid += 1
                right -= 1
    return result

print(threeSum())