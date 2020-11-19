# winning_num = 42
# guess = 1
# num = int(input('Enter any number in 0 to 100'))
# # gave_over = False


# while True:
#     if winning_num == num:
#         print(f'you win ,and you try {guess} time')
#         break
#         # game_over = True
#     elif(num > winning_num):
#         print('too large')
#         guess += 1
#         num = int(input('try again : '))
#     else:
#         print('too less')
#         guess += 1
#         num = int(input('trya agian : '))  
          















import random
winning_num = random.randint(1,100)
guess = 1
num = int(input('Enter any number in 0 to 100'))
game_over = False


while not game_over:
    if winning_num == num:
        print(f'you win ,and you try {guess} time')
        game_over = True
    elif(num > winning_num):
        print('too large')
        guess += 1
        num = int(input('try again : '))
    else:
        print('too less')
        guess += 1
        num = int(input('trya agian : '))  
          

