def reversebit(n):
    reversebinary = ""
    while n > 0:
        reversebinary += str(n%2)   #直接反转
        n = n // 2
    print (f"reversebinary={reversebinary}")

    if len(reversebinary) < 32:
        reversebinary = reversebinary + "0" * (32-len(reversebinary)) #补0
        print (f"reversebinary={reversebinary}")

    result = 0
    for i,v in enumerate(reversed(reversebinary)):  #正常binary读法
        result += int(v) * 2 ** i
    return result
            
print (reversebit(43261596))