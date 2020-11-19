

user = {}

name = input('what is your name: ')
age = input('your age : ')
fav_song = input('Your fav song : ').split(',')
fav_movie = input('Your fav movie : ').split(',')


user['name'] = name
user['age'] = age
user['fav_song'] = fav_song
user['fav_movie'] = fav_movie

# print(user)

for key,value in user.items():
    print(f'{key} : {value}')
    





    