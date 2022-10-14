# 5) Реализуйте алгоритм перемешивания списка.


import random


source_list = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
print('Source list: ' + str(source_list))

for i in range(len(source_list) -1, 0, -1):
    j = random.randint(0, i + 1)
    source_list[i], source_list[j] = source_list[j], source_list[i]
print('Shuffled list: ' + str(source_list))
