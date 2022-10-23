# Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

# !!ВНИМАНИЕ
# !!! не использовать константу math.pi


from decimal import Decimal


num_pi = 0
count = 1
for i in range(10 ** 6):
    if i % 2 == 0:
        num_pi += 4 / count
    else:
        num_pi -= 4 / count
    count += 2
    
num = Decimal(num_pi)
num_d = Decimal(input('Enter the material number denoting accuracy. From 0.1 to 0.0000000001: '))
num_r = num.quantize(Decimal(f'{1 + num_d}'))
print(f'Number π with an accuracy {num_d} signs = {num_r}')
