def discr():
    print('Введите значения a, b, c для вычисления дискреминанта ')
    a = input()
    b = input()
    c = input()
    try:
        dis = int(b) ** 2 - 4 * int(a) * int(c)
    except ValueError:
        print('Неизвестные значения')
    else:
        print('Дискреминант равен', dis)


discr()
