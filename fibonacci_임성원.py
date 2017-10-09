def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a,b = 1,1
        for i in range(n-1):
            a,b = b,a+b
        return a
k = 1
while (k>=0):
    k = int(input("Enter a Number: "))
    if k < 0:
        print("양수를 입력해 주세요.")
        break
    else:
        print(fibo(k))