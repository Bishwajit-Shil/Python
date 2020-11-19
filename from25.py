# ------------------string-index---------------------
lang= "python"
print(lang[5])
print(lang[-1])


# -----------------------string slicing------------
print(lang[:])
print(lang[0:4])
print(lang[-3 :])



# ----------------------step index----------------------------
print(lang[0::2])
print(lang[1::2])
print(lang[-1::-1])
print(lang[::-1]) #as same result


# ------------------len(), upper(), lower(), etc--------------
name= "Nuclear boom"
print(len(name))
print(name.lower())
print(name.upper())
print(name.title())
print(name.count('o'))




# -----------find-----------------
string ='she is beautiful and she is good singer '
print(string.replace( "is" , "was" , 2))

pos= string.find('is')
pos2 =string.find('is', pos + 1)

print(pos2)


# -------------------center method---------------
name= 'Jitshil'
print(name.center(12,'*'))

name= input('iput your name  :')
print(name.center(len(name) + 6,'*'))


