# 3. Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


size_lst = int(input('Enter the number of list elements: '))

num_lst = []
for i in range(size_lst):
    fill_lst = float(input(f'Enter {i + 1} integer elements of the list with index {i}: '))
    num_lst.append(fill_lst)

result_num_lst = []
for i in range(len(num_lst)):
    n = num_lst[i] % 1
    if n != 0:
        result_num_lst.append(n)

maxb = max(result_num_lst)
minb = min(result_num_lst)
print(num_lst, '=>', round((maxb - minb), 2))


# Второй вариант

from random import uniform

num = int(input("Введите количество элементов: "))
num_list = [round(uniform(1, num), 2) for _ in range(num)]
max_num, min_num = round(num_list[0] % 1, 2), round(num_list[0] % 1, 2)
for i in num_list:
    temp = round(i % 1, 2)
    if max_num < temp:
        max_num = temp
    elif min_num > temp:
        min_num = temp
print(f'Исходный список: {num_list}\n'
      f'Максимальное дробное число: {max_num:.2f}\n'
      f'Минимальное дробное число: {min_num:.2f}\n'
      f'Разница между максимальным и минимальным: {max_num - min_num:.2f}')