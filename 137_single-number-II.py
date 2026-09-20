def singlenumber1(nums):
    collection = {}
    for i in range(len(nums)):
        if nums[i] in collection:
            collection[nums[i]] += 1
        else:
            collection[nums[i]] = 1

    for k,v in collection.items():
        if v == 1:
            return k

print (singlenumber1([2,2,3,2]))
print (singlenumber1([0,1,0,1,0,1,99]))
print (singlenumber1([0,0,0,-2147483648]))

def singlenumber2(nums):
    ans = 0
    for k in range(32):
        total = 0
        for num in nums:
            total += (num>>k)&1
        ans += (total % 3) * (2 ** k)
        if ans >= 2 ** 31:
            ans -= 2 ** 32
    return ans

print (singlenumber2([2,2,3,2]))
print (singlenumber2([0,1,0,1,0,1,99]))
print (singlenumber2([0,0,0,-2147483648]))