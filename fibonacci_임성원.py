import time

#재귀함수를 이용한 방법
def fibo(num):
    if num ==1 or num ==2:
        return 1
    else:
        return fibo(num-1) + fibo(num-2)


#점화식을 이용한 방법
def iterfibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        a,b = 1,1
        for i in range(num-1):
            a,b = b,a+b
        return a

nbr = 1
while (nbr>0):
    nbr = int(input("Enter a number: "))
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))