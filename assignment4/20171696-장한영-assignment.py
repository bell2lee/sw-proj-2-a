def Facto(num) :
    if num > 1 :
        return (num * Facto(num-1))
    else :
        return 1
while True:
    num=int(input())
    if num <= -1:
        break
    print(Facto(num))
        
