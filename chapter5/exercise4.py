def odd_even(l):
    odd_even = []
    even = []
    odd = []
    for i in l:
        if i%2 == 0 :
            even.append(i)
        else:
            odd.append(i) 
    odd_even = [even] + [odd]
    # odd_even = [even,odd]
    return odd_even


s= [1,2,3,4,5,6,7,8]
print(odd_even(s))



