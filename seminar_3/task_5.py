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
