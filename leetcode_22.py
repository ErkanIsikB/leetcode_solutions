# Given
# n
# pairs
# of
# parentheses, write
# a
# function
# to
# generate
# all
# combinations
# of
# well - formed
# parentheses.
#
# Example
# 1:
#
# Input: n = 3
# Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
# Example
# 2:
#
# Input: n = 1
# Output: ["()"]
n = 3
def generateParenthesis():
    k = []

    def recur(left, right, possible):
        if left == 0 and right == 0:
            k.append(possible)
        if left > 0:
            recur(left - 1, right, possible + "(")
        if right > left:
            recur(left, right - 1, possible + ")")

    recur(n, n, "")
    return k

print(generateParenthesis())