import math
import time
def fibo(num): #재귀
    if num ==1 or num ==2:
        return 1
    else:
        return fibo(num-1) + fibo(num-2)


def iterfibo(nbr): #반복을 이용
    c=0
    d=1

    for i in range(nbr):
        c,d = d,c+d

    return c



def mathfibo(nbr): # 점화식을 이용


        a= (((1/2* (1+math.sqrt(5))) **nbr+1) -((1/2*(1-math.sqrt(5)))**nbr+1))/math.sqrt(5)
        return (a)

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = mathfibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))