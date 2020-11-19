def num(a):
    for i in range(1,a+1):
        yield (i)

numbers= num(5)
for i in numbers:
    print(i)