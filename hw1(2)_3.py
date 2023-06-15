import math


def koren():
    print('Запишите значкние из которого хотите вывести корень: ')
    num = input()
    try:
        kor = math.sqrt(int(num))
    except ValueError:
        print('Неизвестное значение')
    else:
        print(kor)

if __name__ == '__main__':
    koren()

