def two_sum(nums, target):
    result = {}
    for i, num in enumerate(nums):
        com = target - num
        if com in result:
            return [result[com],i]
        result[num] = i
    return None
print (two_sum([1, 2, 7, 8, 11, 15], 9))