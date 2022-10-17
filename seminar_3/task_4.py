# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


decimal_number = int(input('Enter a decimal number: '))

output_number = decimal_number
binary_number = ''
while decimal_number > 0:
    binary_number += str(decimal_number % 2)
    decimal_number //= 2
print(f'{output_number} -> {binary_number[::-1]}')
