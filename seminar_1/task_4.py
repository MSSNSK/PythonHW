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


# Вариант с семинара:

while True:
    try:
        num_quarter = int(input('Enter the quarter number: '))
        if 1 <= num_quarter <= 4:
            if num_quarter == 1:
                print('X > 0; Y > 0')
                break
            elif num_quarter  == 2:
                print('X < 0; Y > 0')
                break
            elif num_quarter == 3:
                print('X < 0; Y < 0')
                break
            elif num_quarter == 4:
                print('X > 0; Y < 0')
            break
        else:
            print(f'Incorrect number entered - {num_quarter}!')
    except ValueError:
        print('Input error, enter an integer!')


# Ещё вариант с семинара:


num_quarter = int(input('Enter the quarter number: '))

match quarter:
    case 1:
        print('X > 0; Y > 0')
    case 2:
        print('X < 0; Y > 0')
    case 3:
        print('X < 0; Y < 0')
    case 4:
        print('X > 0; Y < 0')
    case _:
        print('There is no such quarter in the Cartesian coordinate system!')
