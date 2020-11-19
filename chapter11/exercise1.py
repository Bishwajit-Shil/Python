def function(*args):
    cubic = []
    if args:
        for i in args:
            cubic.append(i**3)
        return cubic
    else:
        return "You didn't pass any value "

print(function(1,2,3,4))


# ------------------------------------------------------------
def function(*args):
    if args:
        return  [i**3 for i in args]
    else:
        return "You didn't pass any value "

print(function(1,2,3,4))



# ---------------------------without function-------------------------
num = [1,2,3,4]
cubic1 = [i**3 if i else 'any value' for i in num ]
print(cubic1)
