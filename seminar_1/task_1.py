# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет


day_week = int(input('Enter the day of the week: '))
if day_week == 6 or day_week == 7:
    print('Yes, day off.')
elif day_week >= 1 and day_week <= 5:
    print('No, a weekday.')
elif day_week <= 0 or day_week >= 8:
    print('Such a day of the week does not exist!')