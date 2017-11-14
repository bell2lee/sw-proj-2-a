import calcFunctions

numPadList = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=',
]

operatorList = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C', '◀'
]



constantList = {
    'pi': '3.141592',
    '빛의 이동 속도 (m/s)': '3E+8',
    '소리의 이동 속도 (m/s)': '340',
    '태양과의 평균 거리 (km)': '1.5E+8',
}
# calcFunctions.factorial, calcFunctions.decToBin, calcFunctions.binToDec, calcFunctions.decToRoman
a = [calcFunctions.factorial, calcFunctions.decToBin, calcFunctions.binToDec, calcFunctions.decToRoman]
functionList = {
    'factorial (!)': a[0],
    '-> binary': a[1],
    'binary -> dec': a[2],
    '-> roman': a[3],
}