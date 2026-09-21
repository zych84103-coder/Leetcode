def singlenumber(nums):
    single = {}
    for num in nums:
        if num in single:
            single[num] += 1
        else: single[num] = 1

    result = []
    for k,v in single.items():
        if v == 1:
            result.append(k)

    return result

print (singlenumber([1,2,1,3,2,5]))