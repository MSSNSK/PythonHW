# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11


number = input('Enter the number: ')
sum = sum(map(int, number.replace('.', '')))
print (number, '->', sum)
