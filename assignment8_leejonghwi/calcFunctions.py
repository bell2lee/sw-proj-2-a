from math import factorial as fact


#calcFunctions.factorial, calcFunctions.decToBin, calcFunctions.binToDec, calcFunctions.decToRoman
def factorial(numStr):
    '''
    !(3+5)
    :param numStr:
    :return:
    '''
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
