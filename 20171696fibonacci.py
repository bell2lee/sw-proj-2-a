import math

while True:
    number = float(input())+1
    a= (((1/2* (1+math.sqrt(5))) **number+1) -((1/2*(1-math.sqrt(5)))**number+1))/math.sqrt(5)
    print(a)