def countbits(n):
    result = []
    for i in range(0,n+1):
        count = 0
        num = i #循环变量只读不变
        while num > 0:
            binary = num % 2
            num = num//2
            if binary == 1:
                count += 1
        result.append(count)       
    return result
print (countbits(5))