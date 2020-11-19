example = [[1,2,3],[1,2,3],[1,2,3]]

nested = [[i for i in range(1,100)] for j in range(20)]
print(nested)

new_nested = []
for i in range(1,4):
    new_nested.append([1,2,3])

print(new_nested)    