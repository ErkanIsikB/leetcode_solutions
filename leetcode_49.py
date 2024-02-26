# Given
# an
# array
# of
# strings
# strs, group
# the
# anagrams
# together.You
# can
# return the
# answer in any
# order.
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
# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
# Example
# 2:
#
# Input: strs = [""]
# Output: [[""]]
# Example
# 3:
#
# Input: strs = ["a"]
# Output: [["a"]]

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
def groupAnagrams():
    number = {
        "a": 2,
        "b": 3,
        "c": 5,
        "d": 7,
        "e": 11,
        "f": 13,
        "g": 17,
        "h": 19,
        "i": 23,
        "j": 29,
        "k": 31,
        "l": 37,
        "m": 41,
        "n": 43,
        "o": 47,
        "p": 53,
        "r": 59,
        "s": 61,
        "t": 67,
        "u": 71,
        "v": 73,
        "y": 79,
        "z": 83,
        "q": 89,
        "w": 97,
        "x": 101
    }

    anagram_groups = {}

    for word in strs:
        product = 1
        for letter in word:
            product *= number.get(letter, 1)
        if product in anagram_groups:
            anagram_groups[product].append(word)
        else:
            anagram_groups[product] = [word]

    result = list(anagram_groups.values())
    return result
print(groupAnagrams())