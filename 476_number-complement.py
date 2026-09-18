def findcomplement(num):
    flipbinary = ""
    while num > 0:
        flipbinary = str(1 - num % 2) + flipbinary
        num = num // 2

    n = len(flipbinary) - 1
    complement = 0
    i = 0
    while 0 < n:
        complement = int(flipbinary[n]) * (2 ** i) + complement
        #print(f"complement={complement}")
        n -= 1
        i += 1
        #print(f"n={n}")
        #print(f"i={i}")
    return complement

print (findcomplement(5))
print (findcomplement(1))
print (findcomplement(9))