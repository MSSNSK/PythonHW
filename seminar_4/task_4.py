# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше 
# и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем 
# данную итерацию степени
# Записываем результат в файл.

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0


import random


def generate_expr(k):
    lst = [random.randint(-100,100) for i in range(k+1)]
    return lst
    
def create_expr(sp):
    lst = sp[::-1]
    result = ''
    if len(lst) < 1:
        result = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                result += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    result += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                result += f'{lst[i]}x'
                if lst[i+1] != 0:
                    result += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                result += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                result += ' = 0'
    return result

k = int(input("Enter a natural degree k = "))
koef = generate_expr(k)
with open('task4.txt', 'w', encoding='utf-8') as f:
    f.write(create_expr(koef))
print(create_expr(koef))
