#-----------1-----------sum and average-------------------
n = int(input('Enter how many number u input : '))
total = 0
for i in range(1,n+1):
    num = input(f"input number : ")
    total += int(num)

print(f'the total sum :{total}')   
print(f'the total avarege : {total/n}')


# ------------------using function--------------
def sumx(x):
    total = 0
    for i in range(1,x+1):
        num = float(input('enter value : '))
        total += num
    return total 

n = int(input('Enter number of data set : '))
sumx= sumx(n)
print(f'the total sum  : {sumx} and the average : {sumx/n}')






# ----------2-------- sum for 1/n -----------------------
n = int(input('enter the value of n : '))

total = 0
for i in range(1,n+1):
    total += 1.0/i
print(f' the calculated sum : {total}')   


# ----2----using function-------
def sumx(x):
    total = 0
    for i in range(1,x+1):
        total += 1.0/i
    return total    
n = int(input('enter the value of n : '))
print(f'total : {sumx(n)}') 





# ----------3------------triangle---------------------------
a= int(input('Enter a : '))
b= int(input('Enter b : '))
c= int(input('Enter c : '))


if(a+b<c or a+c<b):
    print('invalid length . ')   
else:
    perimeter= a+b+c
    s = perimeter/2
    area = pow((s*(s-a)*(s-b)*(s-c)),0.5)
    print(f'the tirangle perimeter : {perimeter}')
    print(f'the triangle area : {area}')    





# ------------------------gamma--------------------------
#------------gamma=h1/(h1-h2)---------
n = int(input('How many data set want to input : '))

sumh1 = 0
sumh2 = 0
for i in range(1,n+1):
    h1= float(input('Enter the values of h1 : '))
    sumh1 += h1    
print('\n')

for i in range(1,n+1):
    h2= float(input('Enter the values of h2 : '))    
    sumh2 += h2
avgh1 = sumh1/n
avgh2 = sumh2/n
 
print(f'the calculated gamma {avgh1/(avgh1-avgh2)}') 


#-------------------------using function---------------------
def sumx(x):
    sumx = 0
    for i in range(1,x+1):
        h = float(input('Enter the value : '))
        sumx += h
    return sumx

n = int(input('How many data set want to input : '))     
avgh1 = sumx(n)/n
print('\n')
avgh2 = sumx(n)/n
print(f'the calculated gamma is : {avgh1/(avgh1-avgh2)}')




# # ----------------------standard diviation= sqrt(x - average_x)/n)------------
n = int(input('Enter number of data set : '))

sumx= 0
for i in range(1,n+1):
    x = float(input('Enter value of x : '))
    sumx += x
avgx = sumx/n

ssd = 0
for i in range(1,n+1):
    ssd += (x - avgx)**2
std = (ssd/n)**0.5

print(f'The calculated standard diviation is : {std}')