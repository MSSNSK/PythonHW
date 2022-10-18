# 1) Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
#
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


number = input('Enter the number: ')

result = 0
for i in number:
    if '-' != i != ".":
        result += int(i)
print(number, '->', result)


# Вариант с семинара через isdecimal или isdigit:

print(sum(map(int, (c for c in input('Enter the number: ') if c.isdecimal()))))

# или isdigit()


# Второй вариант с семинара:

flo_at = input('Enter the number: ')
number_arr = flo_at.split('.')

full_num = ''
if len(number_arr) != 1:
    full_num = number_arr[0] + number_arr[1]
else:
    full_num = number_arr[0]

sum_nums = 0
for i in full_num:
    sum_nums += int(i)
print(sum_nums)


# Третий вариант с семинара через Decimal:

from decimal import *


num = Decimal(12.345)
getcontext().prec = 10

while True:
    if num % 10 != 0:
        num *= 10
    else:
        num = int(num //10)
        break

num_sum = 0
while num != 0:
    num_sum += num % 10
    num //= 10
print(num_sum)


# Четвёртый вариант с семинара:

num = input('Enter the number: ')
after_com = len(num) - num.find('.')
num = int(float(num) * (10 ** after_com))

num_sum = 0
while num != 0:
    num_sum += num % 10
    num //= 10
print(num_sum)


# Пятый вариант с семинара:

num, summ = input('Enter the number: '), 0
num = num.replace('-', '')
num = num.replace(',', '')
num = num.replace('.', '')
for i in range(len(num)):
    summ += int(num[i])
print(summ)


# Вариант (преподователя) с семинара через Decimal:

from decimal import Decimal


num = Decimal(input('Enter the number: '))

while int(num) != num:
    num *= 10

result = 0
while num:
    result += num % 10
    num //= 10
print(result)
