while True:
    n = int(input("Enter a Number:"))
    a = 1
    if n < 0 :
        break
    elif n == 0 :
        print("1")
    else:
        for i in range(1,n+1):
            a *= i
        print(n,'!=',a)
