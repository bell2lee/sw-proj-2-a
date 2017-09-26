
def fact(n,m,s):
    if n <=1 or m <1 :
        return s

    elif n >=2 and m>=1:
        s *= n/m
        n= n-1
        m= m-1

        return fact(n, m, s)

n = int(input())
m = int(input())
s = 1

print(fact(n,m,s))