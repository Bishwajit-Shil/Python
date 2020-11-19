
def febonacci(n):
    a = 0
    b = 1
    if n == 1:
        print(a) 
    elif n == 2:
        print(a, b)
    else:
        print(a,b, end= ' ')
        for i in range(1,n-1):
            c =a+b
            a = b
            b = c
            print(b, end=' ')        
febonacci(100)            