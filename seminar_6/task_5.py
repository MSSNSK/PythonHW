# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


import math


num_lst = list(map(int, input('Enter the numbers, separated by a "Space": ').split()))
print(num_lst, '=>', list([a * b for a, b in zip(num_lst[0:math.ceil(len(num_lst) / 2)],num_lst[::-1])]))
