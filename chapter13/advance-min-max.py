number = [1,2,3,4,5,6]
print(max(number))
print(min(number))


def func(item):
    return len(item)
names=['sobro','rohitss','sobuj roy']
# nn = max(names, key= func)
nn = min(names, key= lambda item :len(item))
print(nn)


students=[
    {'name':'jitshil','age':21},
    {'name':'Ab Rayhan','age':20},
    {'name':'Nazmul mama','age':23},
    {'name':'Raihan ali','age':21},
    {'name':'Sadman','age':21},
    {'name':'milon','age':22},
    {'name':'tohid','age':22},
]
print(max(students, key =lambda item:item.get('age')))
