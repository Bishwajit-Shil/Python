fruit1 = ['pinaple','mango','apple']
fruit1.sort()
print(fruit1)


fruit2 = ('pinaple','mango','apple')
print(sorted(fruit2))


guiter=[
    {'name': 'yamha','price':8000},
    {'name': 'singnature','price':6000},
    {'name': 'electric','price':22000}
]
print(sorted(guiter, key=lambda item:item.get('price'),reverse = True))