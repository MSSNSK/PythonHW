# 2. Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


sign = True

for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not (x or y or z) == (not x and not y and not z)) != sign:
                print('False.')
                break
else:
    print('True.')


# Вариант с семинара через кортеж:

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            print((x, y, z), '- True.' if not (x or y or z) == (not x and not y and not z) else '- False.')


# Варианты с семинара в одну строку:

print(*(not (x or y or z) == (not x and not y and not z) for z in range(2) for y in range(2)
        for x in range(2)), sep='\n')



from itertools import product


print(all(not (x or y or z) == (not x and not y and not z) for x, y, z in product(*((True, False),) * 3, )))