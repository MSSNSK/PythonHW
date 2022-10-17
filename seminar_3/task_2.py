# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


size_lst = int(input('Enter the number of list elements: '))

num_lst = []
for i in range(size_lst):
    fill_lst = int(input(f'Enter {i + 1} integer elements of the list with index {i}: '))
    num_lst.append(fill_lst)

mult = []
for i in range((size_lst + 1) // 2):
    if num_lst[i] != num_lst[-i - 1] > num_lst[i]: 
        mult.append(num_lst[i] * num_lst[-i - 1])
    if num_lst[i] == num_lst[-i - 1]:
        mult.append(num_lst[i] * num_lst[i])
        break
print(f'{num_lst} => {mult}')
