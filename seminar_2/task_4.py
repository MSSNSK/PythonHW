# 4) Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры .


from random import randint


n = int(input('Enter the number of list elements: '))

sequence_number = []
for i in range(n):
    sequence_number.append(randint(-n, n + 1))
print(sequence_number)

a = int(input('Enter the index of the first element (multiplier): '))
b = int(input('Enter the index of the second element (multiplier): '))

for i in range(len(sequence_number)):
    mult = sequence_number[a] * sequence_number[b]
print('Mult of elements:', mult)
