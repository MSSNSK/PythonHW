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
else:
    print('Such a day of the week does not exist!')


# Вариант с семинара через кортеж:

days_week = 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
day  = int(input('Enter the day of the week: '))
if 0 < day < 8:
    print(f'This day of the week - {days_week[day - 1]}')
else:
    print('Such a day of the week does not exist!')


# Вариант с семинара через тернарный оператор:

day = int(input('Enter the day of the week: '))
print('Yes' if day in [6, 7] else 'No' if day in range(1, 6) else 'Such a day of the week does not exist!')


# Вариант с семинара через match/case:

day_week = int(input('Enter the day of the week: '))
match day_week:
    case 6 | 7:
        print('Yes, day off.')
    case day_week if day_week in range(1, 6):
        print('No, a weekday.')
    case _:
        print('Such a day of the week does not exist!')


# Вариант с семинара через строку:

day_week = (input('Enter the day of the week: '))
if day_week in '12345':
    print('No, a weekday.')
elif day_week in '67':
    print('Yes, day off.')
else:
    print('Such a day of the week does not exist!')