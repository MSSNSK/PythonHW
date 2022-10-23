# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0


from random import randint
import ast

def generate_expr(k, t):
    result = ''
    result2 = []
    while k >= 0:
        rand = randint(0, 100)
        if k == 1:
            k_op = 'x'
        else:
            k_op = f'x^{k}'
        if rand > 1 and k != 0:
            result += f'{rand}{k_op}' + ' + '
        elif rand == 1 and k != 0:
            result += f'{k_op}' + ' + '
        result2.append((rand, k))
        k -= 1
    if t == 't4':
        return result + f'{randint(0, 100)} = 0'
    else:
        return f'{result2}'


def create_expr(coeff):
    result = ''
    for i in range(0, len(coeff), 2):
        k = coeff[i + 1]
        coef = coeff[i]
        if k == 1:
            k_op = 'x'
        elif k == 0:
            k_op = ''
        else:
            k_op = f'x^{k}'
        if coef > 1 and k != 0:
            result += f'{coef}{k_op}' + ' + '
        elif coef == 1:
            result += f'{coef}' + ' + '
        else:
            result += f'{coef} = 0'
    return result

exp_1 = ast.literal_eval(open('task5_1.txt', 'r').read())
exp_2 = ast.literal_eval(open('task5_2.txt', 'r').read())
fst, snd = [], []
result = []
for i in range(len(exp_1)):
    result += (exp_1[i][0] + exp_2[i][0], exp_1[i][1])
for i in range(len(exp_1)):
    fst.append(exp_1[i][0])
    fst.append(exp_1[i][1])
    snd.append(exp_2[i][0])
    snd.append(exp_2[i][1])
print(f'The first polynomial: {create_expr(fst)}\n'
      f'The second polynomial: {create_expr(snd)}\n'
      f'The amount of polynomials: {create_expr(result)}')