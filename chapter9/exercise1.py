
def reverse(l):
    reverse = [i[::-1] for i in l ]
    return reverse

l = ['abc','def','ghi']
print(reverse(l))