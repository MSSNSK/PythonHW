# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг 
# после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у 
# своего конкурента?

# b) Подумайте как наделить бота ""интеллектом""



from random import randint


def input_dat(name):
    x = int(input(f'{name}, enter the number of sweets that you take from 1 to 28: '))
    while x < 1 or x > 28:
        x = int(input(f'{name}, enter the correct amount of sweet(s): '))
    return x

def p_print(name, k, count, value):
    print(f'{name} took {k}, now with him {count}, left on the table {value} sweet(s).')

def bot_calc(value):
    k = randint(1,29)
    while value-k <= 28 and value > 29:
        k = randint(1,29)
    return k

player1 = input('Enter the name of the first player: ')
player2 = 'BOT'
sweet = 2021
flag = randint(0, 2)
if flag:
    print(f'The first walks {player1}!')
else:
    print(f'The first walks {player2}!')

count1 = 0 
count2 = 0

while sweet > 28:
    if flag:
        k = input_dat(player1)
        count1 += k
        sweet -= k
        flag = False
        p_print(player1, k, count1, sweet)
    else:
        k = bot_calc(sweet)
        count2 += k
        sweet -= k
        flag = True
        p_print(player2, k, count2, sweet)

if flag:
    print(f'Won {player1}!')
else:
    print(f'Won {player2}!')
