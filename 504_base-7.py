def base7(num):
    if num == 0:
        return "0"

    negative = num < 0
    num = abs(num)

    result = ""
    while num > 0:
        digit = num % 7
        result = str(digit) + result
        num = num//7
        print (f" this loop: digit={digit}, num={num}, result={result}")

    if negative:
        result = "-" + result

    return result

print (base7(100))
print (base7(1234))