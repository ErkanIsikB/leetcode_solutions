# Given
# a
# string
# s
# containing
# just
# the
# characters
# '(', ')', '{', '}', '[' and ']', determine if the
# input
# string is valid.
#
# An
# input
# string is valid if:
#
# Open
# brackets
# must
# be
# closed
# by
# the
# same
# type
# of
# brackets.
# Open
# brackets
# must
# be
# closed in the
# correct
# order.
# Every
# close
# bracket
# has
# a
# corresponding
# open
# bracket
# of
# the
# same
# type.
#
# Example
# 1:
#
# Input: s = "()"
# Output: true
# Example
# 2:
#
# Input: s = "()[]{}"
# Output: true
# Example
# 3:
#
# Input: s = "(]"
# Output: false
s = "()[]{}"
def isValid():
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}

    for c in s:
        if c in brackets:
            stack.append(c)
        elif stack and c == brackets[stack.pop()]:
            continue
        else:
            return False

    return not stack

print(isValid())