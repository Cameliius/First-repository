password = 235
user_password = int(input('Введите пароль: '))
while password != user_password:
    print('Не верный пароль!')
    user_password = int(input('Введите пароль: '))
print('Добро пожаловать')
