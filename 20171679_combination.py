
'''def factorial(n):
    else1
        return n * factorial(n - 1)

n = int(input())
m = int(input())

s = int(factorial(n) / (factorial(m) * factorial(n - m)))

print(s)

https://en.wikipedia.org/wiki/Combination

'''


def combination(n, m):
    if m > n:
        return 0
    elif m == 0 or m == n:
        return 1
    else:
        return combination(n-1, m) + combination(n-1, m-1)


while True:
    n = int(input("Enter n : "))
    if n == -1:
        break
    m = int(input("Enter m : "))

    print(combination(n, m))