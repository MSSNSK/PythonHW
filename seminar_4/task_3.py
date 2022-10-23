# Задайте последовательность цифр. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []


numbers_list = list(map(int, input('Enter the sequence of numbers through the "Space" and click "Enter": ').split()))
unique_list = [i for i in set(numbers_list) if numbers_list.count(i) == 1]
print(unique_list)