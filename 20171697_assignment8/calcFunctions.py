from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    return 'dec -> Roman'

def fixThefloatpoint(numStr):
    integer_part = int(numStr)
    decimal_part = str(numStr - integer_part)
    if float(decimal_part) != 0:
        for i in range(len(decimal_part) - 2):
            if decimal_part[i] == decimal_part[i + 1] == decimal_part[i + 2]:
                conclusion_num = integer_part + round(float(decimal_part[0:i + 1]), i - 2)
                result = str(conclusion_num)
                break
    else:
        result = str(integer_part)
    return result