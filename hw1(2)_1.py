def calculate():
    print('Укажите интерисующую вас операцию (+, -, *, /)')

    operation = input()

    if operation == '*':
        num1 = input('Введите первое число ')
        num2 = input('Введите второе число ')
        try:
            res = int(num1) * int(num2)
        except ValueError:
            print('Неизвестные значения')
        else:
            print(res)

    if operation == '/':
        num1 = input('Введите первое число ')
        num2 = input('Введите второе число ')
        try:
            res = int(num1) / int(num2)
        except ValueError:
            print('Неизвестные значения')
        else:
            print(res)

    if operation == '+':
        num1 = input('Введите первое число ')
        num2 = input('Введите второе число ')
        try:
            res = int(num1) + int(num2)
        except ValueError:
            print('Неизвестные значения')
        else:
            print(res)

    if operation == '-':
        num1 = input('Введите первое число ')
        num2 = input('Введите второе число ')
        try:
            res = int(num1) - int(num2)
        except ValueError:
            print('Неизвестные значения')
        else:
            print(res)


calculate()
