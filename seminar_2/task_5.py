# 5) Реализуйте алгоритм перемешивания списка.


import random


source_list = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
print('Source list: ' + str(source_list))

for i in range(len(source_list) -1, 0, -1):
    j = random.randint(0, i + 1)
    source_list[i], source_list[j] = source_list[j], source_list[i]
print('Shuffled list: ' + str(source_list))


# Вариант с семинара:

import random


lst = list(range(10))
random.shuffle(lst)

print(lst)


# Второй вариант с семинара:

import random


lst = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
print(f'Original -->', lst)
print('Random -->', random. sample(lst, len(lst)))


# Третий вариант с семинара через время:

lst = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']

def my_Random(lst):
    import time
    value = round(time.time() * 1000) % 10 
    for i in range(len(lst)):
        if value < len(lst):
            lst[i], lst[-value] = lst[-value], lst[i]
            value = int((((time.time() * 1000) % 1000) // 100 - i))
        else:
            value = 0
    return lst

print('Random -->', my_Random(lst))
