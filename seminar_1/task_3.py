# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


x = int(input('Enter X: '))
y = int(input('Enter Y: '))

if x > 0 < y:
    print('1 quarter.')
elif x < 0 < y:
    print('2 quarter.')
elif x < 0 > y:
    print('3 quarter.')
elif x > 0 > y:
    print('4 quarter.')
elif x == 0 != y:
    print('The point is on the ordinate axis.')
elif y == 0 != x:
    print('The point is on the abscissa axis.')
else:
    print('Origin!')