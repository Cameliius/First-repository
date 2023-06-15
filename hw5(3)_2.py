# Извините, я в одном из заданий допустила ошибку(вместо бесконечного итератора, я написала бесконечный гениратор), поэтому в этом номере сразу два задания

# Задание 2
import random


class RandomIter:
    def __next__(self):
        return random.randint(1, 9)

    def __iter__(self):
        return self


random_iter = RandomIter()

for i in random_iter:
    print(i)


# # Задание 1
# class MyFile:
#     def __init__(self, file_name, mode, encode='utf-8'):
#         self.file_name = file_name
#         self.mode = mode
#         self.encode = encode
#
#     def __enter__(self):
#         self.file = open(file=self.file_name, mode=self.mode, encoding=self.encode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#
# with MyFile('file.txt', 'r') as f:
#     print(f.read())
