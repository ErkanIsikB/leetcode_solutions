# Given
# two
# strings
# s and t,
# return true if t is an
# anagram
# of
# s, and false
# otherwise.
#
# An
# Anagram is a
# word or phrase
# formed
# by
# rearranging
# the
# letters
# of
# a
# different
# word or phrase, typically
# using
# all
# the
# original
# letters
# exactly
# once.
#
# Example
# 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example
# 2:
#
# Input: s = "rat", t = "car"
# Output: false
def isAnagram():
    s = "anagram"
    t = "nagaram"
    if len(t) != len(s):
        return False
    i = 0
    while i < len(t):
        try:
            s = s.replace(t[i], "", 1)
        except:
            return False
        i += 1
    if len(s) == 0:
        return True


print(isAnagram())