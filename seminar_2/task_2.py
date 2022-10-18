# 2) Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
#
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


number = int(input('Enter the number N: '))

factorial = 1
for i in range(1, number + 1):
    factorial *= i
    print(factorial, end=' ')


# Вариант с семинара через for:

while True:
    try:
        n = int(input('Enter the number N: '))
    except ValueError:
        print('Incorrect input!')
        break

result_iterator = [1]
for i in range(1, n + 1):
    result_iterator.append(i * result_iterator[- 1])
print(result_iterator[1:])


# Вариант с семинара через while:

N = int(input('Enter the number N: '))
factorial_N = []

n = 1
factorial_n = 1
while n <= N:
    factorial_n *= n
    n += 1
    factorial_N.append(factorial_n)
print(factorial_N)


# Вариант с семинара через рекурсивную анонимную (безымянную) функцию lambda:

N = int(input('Enter the number N: '))

factorial = lambda x: x if x == 1 else x * factorial(x - 1)
print([factorial(i) for i in range(1, N + 1)])


# Вариант с семинара через генератор:

N = int(input('Enter the number N: '))

def fact(N):
    last = 1
    for i in range(1, N + 1):
        last *= i
        yield last

result = fact(N)
lst = list(result)
print(lst)
