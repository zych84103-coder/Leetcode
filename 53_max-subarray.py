def max_subarray(nums):
    curnums = nums[0]
    maxnums = nums[0]

    for num in nums[1:]:
        curnums = max(num, curnums + num)
        maxnums = max(curnums, maxnums)
    return maxnums
# 测试
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(max_subarray([1]))                                  # 1
print(max_subarray([5, 4, -1, 7, 8]))                     # 23