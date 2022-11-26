import math

def isPerfectSquare(num):
    s =int(math.sqrt(num))
    return s*s == num

def isFibonacciNumber(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
flag=True
while True:
    n = list(map(int,input("Enter the number you want to check : ").split(" and ")))
    count=0
    for i in n:
        if(isFibonacciNumber(n[count]) == True):
            print(n[count] ," is valid ")
        else:
            print(n[count]  ,"  is invalid ")
        count+=1
										
