def integertoroman(num):
    values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    symbols = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    result = ""
    for v,s in zip(values,symbols):
        count = num // v
        result += s * count
        num %= v
    return result

#1-3999
print (integertoroman(1234))
print (integertoroman(395))
print (integertoroman(456))