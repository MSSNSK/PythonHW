# Задайте натуральное число N. Напишите программу, которая составит список 
# простых множителей числа N.


num = int(input('Enter a natural number: '))
print(f'The number: {num}')

factors = []
i = 2
while i * i <= num:
    while num % i == 0:
        num //= i
        factors.append(i)
    i += 1
else:
    factors.append(num)
print(f'Has the following simple factors: {factors}')
