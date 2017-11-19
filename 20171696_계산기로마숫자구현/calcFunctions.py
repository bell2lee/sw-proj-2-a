from math import factorial as fact




romans = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]
romans2 = {
'M':1000,'D':500,'C'
:100 ,  'L': 50,'X'
:10 ,  'V': 5,
'I':1

}

def factorial(numStr):
    try:
        n = eval(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = eval(numStr)
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

    try:
        numStr = int(numStr)
        result = ''
        for value, letters in romans:
            while numStr >= value:
                result += letters
                numStr-= value
        return result
    except: print("Error")

def RomanTodec(numStr):
    try:
        result2 = 0
        for i in range(len(numStr)-1):

            if romans2[numStr[i]] < romans2[numStr[i + 1]]:
                result2 -= romans2[numStr[i]]
            else:result2 += romans2[numStr[i]]
        result2+=romans2[numStr[len(numStr)-1]]
        return result2


    except: print("Error")






calfunc=[factorial,decToBin,binToDec,decToRoman,RomanTodec]