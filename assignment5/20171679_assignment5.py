import time

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
    # 반복문으로 피보나치 수열 구현
    # 1 1 2 3 5 8 12 21

    if n <= 1:
        return n
    else:
        a, b = 1, 1
        for i in range(1, n):
            a, b = b, a + b
        return a


if __name__ == "__main__":
    while True:
        nbr = int(input("Enter a number: "))
        if nbr == -1:
            break

        ts = time.time()
        fibonum = fibo(nbr)
        ts = time.time() - ts
        print("Fibo (%d)=%d, time %.6f" %(nbr, fibonum, ts))

        ts = time.time()
        fibonum = iterfibo(nbr)
        ts = time.time() - ts
        print("InterFibo (%d)=%d, time %.6f" %(nbr, fibonum, ts))