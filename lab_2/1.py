x = float(input('Введіть координату x: '))
y = float(input('Введіть координату y: '))


if x == 0 and y == 0:
    print('Точка розташована в початку координат.')
elif x == 0:
    print('Точка лежить на осі Y.')
elif y == 0:
    print('Точка лежить на осі X.')
else:
    if x > 0:
        if y > 0:
            print('Точка розташована в першому квадранті.')
        else:
            print('Точка розташована в четвертому квадранті.')
    else:
        if y > 0:
            print('Точка розташована в другому квадранті.')
        else:
            print('Точка розташована в третьому квадранті.')
