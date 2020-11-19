import time
t1=time.time()
print('this is the first line')
for i in range(1,10):
    print(i)
print('this is the last line') 
t2=time.time()
print(t2-t1)   

