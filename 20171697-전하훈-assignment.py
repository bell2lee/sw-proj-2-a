while True :
    num = int(input("숫자를 입력하세요 : "))
    if num == -1 :
        print('상수를 입력하십시오!')
        break
    s = 1
    for i in range(1,num+1) :
        s *= i
    print(num,'팩터리얼은 ',s,'입니다.')