
def cubic_finder(n):
    cubes = {}
    for i in range(1,n+1):
        cubes[i] = i**3
        print(cubes)
    return cubes    

n = int(input('Enter n : '))
print(cubic_finder(n))    
