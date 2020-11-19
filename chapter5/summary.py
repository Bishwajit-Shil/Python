mixed = [1,2,3,[3,4,5,5],'jitshil',0 ,'seven']

# -----------------for add-----------
print(mixed[0])
print(mixed[3])

mixed.append(3)
mixed.append([4,3,2])

mixed.extend([4,3,2])

mixed.insert(1,'gumaw')

l = mixed + mixed
# ------------------for remove----------

mixed.pop(4)

mixed.remove('seven')

del mixed[2]

# -------------print every element--------------
for i in mixed:
    print(i)

