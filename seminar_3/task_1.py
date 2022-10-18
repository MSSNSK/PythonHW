# 1. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


size_lst = int(input('Enter the number of list elements: '))

num_lst = []
for i in range(size_lst):
    fill_lst = int(input(f'Enter {i + 1} integer elements of the list with index {i}: '))
    num_lst.append(fill_lst)

nums_odd_indexes = []
summ = 0
for i in range(1, len(num_lst), 2):
    nums_odd_indexes.append(num_lst[i])
    summ += num_lst[i]
print(f'{num_lst} -> in odd positions elements = {nums_odd_indexes}, answer: {summ}')


# Второй вариант

from random import randint


num = int(input("Введите количество элементов: "))
num_list = [randint(-num, num) for _ in range(num)]
num_sum = sum(num_list[1::2])
print(f"Исходный список: {num_list}\n"
      f"Элементы на нечётных позициях: {num_list[1::2]}\n"
      f"Их сумма: {num_sum}")
      