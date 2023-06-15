numbers = []
for i in range(10):
    num = int(input('Введите число '))
    numbers.append(num)
chet = [num for num in numbers if num % 2 == 0]
nechet = [num for num in numbers if num % 2 != 0]
print(chet)
print(nechet)
