# 1) Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
#
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


number = input('Enter the number: ')

result = 0
for i in str(number):
    if i != ".":
        result += int(i) 
print(number, '->', result)
