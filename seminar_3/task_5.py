# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для
# отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


size_lst = int(input('Enter the number: '))

fibonacci_numbers = []
num1 = 1
num2 = 1
for i in range(size_lst):
    fibonacci_numbers.append(num1)
    num1, num2 = num2, num1 + num2

num1 = 0
num2 = 1
for i in range(size_lst + 1):
    fibonacci_numbers.insert(0, num1)
    num1, num2 = num2, num1 - num2
print(f'For k = {size_lst} the list will look like this:')
print(fibonacci_numbers)


# Вариант вычисления двух веток и соединение их:

from functools import cache


def fibonacci(fib, start, pos):
    result = start
    if fib == 0 or fib == 1:
        return 0
    if pos == '+':
        for i in range(2, fib):
            2
            result.append(result[i - 2] + result[i - 1])
    elif pos == '-':
        for i in range(2, fib):
            result.append(result[i - 2] - result[i - 1])
    return result


fib_num = int(input("Введите число: "))
fib_list = [0]
fib_list = fibonacci(fib_num, [1, -1], '-')[::-1] + fib_list
fib_list = fib_list + fibonacci(fib_num, [1, 1], '+')
print(fib_list)


# Вариант с вычислением почти-что на лету:

def fibonacci(fib, start):
    result1 = start
    result2 = result1.copy()[:0:-1]
    for i in range(2, fib):
        if i % 2 == 0:
            result1.append(result1[i - 2] + result1[i - 1])
            result2.insert(0, -result1[i])
        else:
            result1.append(result1[i - 2] + result1[i - 1])
            result2.insert(0, result1[i])
    return result2 + result1


fib_num = int(input("Введите число: "))
fib_list = [0, 1]
fib_list = fibonacci(fib_num, fib_list)
print(fib_list)


# Чуть проще:

def fibonacci(fib, start):
    result = start
    for i in range(2, fib + 1):
        if i % 2 == 0:
            result.append(result[-2] + result[-1])
            result.insert(0, -result[-1])
        else:
            result.append(result[-2] + result[-1])
            result.insert(0, result[-1])
    return result


fib_num = int(input("Введите число: "))
fib_list = [1, 0, 1]
fib_list = fibonacci(fib_num, fib_list)
print(fib_list)


# Рекурсия:

from functools import cache


@cache
def fibonacci(fb):
    if fb == 1 or fb == 2:
        return 1
    else:
        return fibonacci(fb - 1) + fibonacci(fb - 2)

fib_num = int(input("Введите число: "))
fib_list = [0]
for i in range(1, fib_num + 1):
    fib = fibonacci(i)
    fib_list = [((-1) ** (i + 1)) * fib] + fib_list + [fib]
print(fib_list)
