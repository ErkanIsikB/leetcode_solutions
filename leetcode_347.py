# Given
# an
# integer
# array
# nums and an
# integer
# k,
# return the
# k
# most
# frequent
# elements.You
# may
# return the
# answer in any
# order.
#
# Example
# 1:
#
# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2]
# Example
# 2:
#
# Input: nums = [1], k = 1
# Output: [1]

nums = [1, 1, 1, 2, 2, 3]
k = 2
def topKFrequent():
    count_dict = {}
    for number in nums:
        count_dict[number] = count_dict.get(number, 0) + 1

    sorted_counts = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    result = [x[0] for x in sorted_counts[:k]]
    return result

print(topKFrequent())