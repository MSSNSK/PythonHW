# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).


num_quarter = int(input('Enter the quarter number: '))

if num_quarter == 1:
    print('X > 0; Y > 0')
elif num_quarter == 2:
    print('X < 0; Y > 0')
elif num_quarter == 3:
    print('X < 0; Y < 0')
elif num_quarter == 4:
    print('X > 0; Y < 0')
else:
    print('There is no such quarter in the Cartesian coordinate system!')