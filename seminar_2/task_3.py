# 3) Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
#
# Пример:
#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06


n = int(input('Enter the number of list numbers: '))

sequence_number = []
for i in range(1, n + 1):
    sequence_number.append(round((1 + 1 / i) ** i, 2))
print('Sequence of numbers:', sequence_number)
print('Sum of numbers:', round(sum(sequence_number), 2))
