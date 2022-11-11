# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


from functools import reduce


def dot_range(dot_1, dot_2):
     range = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(dot_1, dot_2))))
     return round(range, 2)

dot_1 = list(map(int, input('Enter the two coordinates of the first point "A", separated by a "Space": ').split())) 
dot_2 = list(map(int, input('Enter the two coordinates of the second point "B", separated by a "Space": ').split()))

print(f'A {dot_1}; B {dot_2} -> {dot_range(dot_1, dot_2)}')
