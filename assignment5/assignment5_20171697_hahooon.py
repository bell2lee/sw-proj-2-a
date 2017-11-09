import time

#리스트와 반복을 이용한 피보나치 구하기
def interfibo_lis(num):
    answer = 0
    lis = [num]
    while lis[0] > 0 :
        lis.append(lis[0]-1)
        lis.append(lis[0]-2)
        if lis[0] == 1:
            answer += 1
        del lis[0]
        lis.sort(reverse = True)

    return answer

#단순한 점화식 반복을 이용한 피보나치 구하기
def interfibo(num) :
    if num == 1 :
        return 1
    else :
        a0 = 0
        a1 = 1
        answer = 0
        for i in range(num-1) :
            answer = a0 + a1
            a0 = a1
            a1 = answer

    return answer

#재귀적 피보나치 구하기
def fibo(num):
    if num == 1 or num == 2 :
        return 1
    else :
        return fibo(num-1) + fibo(num-2)

num = int(input('Enter a number : '))
while num > 0 :
    ts = time.time()
    fibonumber = interfibo(num)
    ts = time.time() - ts
    print("Interfibo(%d) = %d, time = %.6f" %(num, fibonumber, ts))
    ts = time.time()
    fibonumber = interfibo_lis(num)
    ts = time.time() - ts
    print("Interfibo_lis(%d) = %d, time = %.6f" %(num, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(num)
    ts = time.time() - ts
    print("Fibo(%d) = %d, time = %.6f" %(num, fibonumber, ts))
    num = int(input('Enter a number : '))