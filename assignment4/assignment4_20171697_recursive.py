def combination(n,m):
    if n >= 0 and m >= 0:
        if n > 0 and m == 0 or n == m :
            return 1
        elif n == 0:
            return 0
        else:
            return combination(n-1,m-1) + combination(n-1,m)

n = 1
m = 0
while n > 0 and m >= 0 :
    n = int(input('N에 해당하는 숫자를 입력하십시오 :'))
    m = int(input('M에 해당하는 숫자를 입력하십시오 :'))
    if n/2 < m :
        m = n - m
    if n < 0 or m < 0:
        print('N과M은 상수이어야 합니다.')
    print(combination(n,m))