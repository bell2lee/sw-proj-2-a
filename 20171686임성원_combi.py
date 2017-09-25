# 수학적으로 짠 코드
'''
def combination(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * combination(n-1)


n = int(input("n의 값을 입력해 주세요:"))
m = int(input("m의 값을 입력해 주세요:"))
c = combination(n) / (combination(m)*combination(n-m))
print(n,"C",m, "=", c)
'''

#재귀함수로 짠 코드
def nCr(n,k):
    if k ==0:
        return 1
    elif n<k: # k가 n보다 커지면 정의할 수 없으므로 0으로 리턴되게 설정 함.
        return 0
    else:
        return nCr(n-1, k-1) + nCr(n-1,k)

n = int(input("n의 값을 입력해 주세요:"))
k = int(input("k의 값을 입력해 주세요:"))
print(nCr(n,k))