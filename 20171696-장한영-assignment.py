def Facto(num) :
    if num > 1 :
        return (num * Facto(num-1))
    else :
        return 1
while True:
    num=int(input())
    print(Facto(num))
