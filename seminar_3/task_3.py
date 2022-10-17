# 3. Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


size_lst = int(input('Enter the number of list elements: '))

num_lst = []
for i in range(size_lst):
    fill_lst = float(input(f'Enter {i + 1} integer elements of the list with index {i}: '))
    num_lst.append(fill_lst)

min_fract = (num_lst[0] - int(num_lst[0]))
max_fract = (num_lst[1] - int(num_lst[1]))
for i in range(len(num_lst)):
    if (num_lst[i] - int(num_lst[i])) > max_fract:
        max_fract = num_lst[i]
    elif (num_lst[i] - int(num_lst[i])) < min_fract:
        min_fract = num_lst[i]
print(num_lst, '=>', round((max_fract - int(max_fract)) - (min_fract - int(min_fract)), 2))
