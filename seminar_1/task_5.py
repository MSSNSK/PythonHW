# 5. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


from math import sqrt


x1 = int(input('Enter X1: '))
y1 = int(input('Enter Y1: '))
x2 = int(input('Enter X2: '))
y2 = int(input('Enter Y2: '))

result = sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
print(round(result, 2))


# Вариант с семинара:

x1 = int(input('Enter X1: '))
y1 = int(input('Enter Y1: '))
x2 = int(input('Enter X2: '))
y2 = int(input('Enter Y2: '))

print('Distance -', round((((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5, 2))
