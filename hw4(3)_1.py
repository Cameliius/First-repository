# a = [x for  x in range(1, 10000000)]
#
# print(a)

# a = ( x for  x in range(1, 10000000))
# print(a)
# for i in a:
#     print(i)


# def my_lazy_gen():
#     for x in range(100):
#         yield x
#
# print(my_lazy_gen())
#
# for i in my_lazy_gen():
#     print(i)


# file = open('file.txt', 'w')
# file.write(['Hello!', 254, 52])
# file.close()

# lst = []
# for  i in range(10000):
#     file = open('file.txt', 'w')
#     lst.append(file)
#     file.close()


# with print('file.txt', 'w') as file:
#     file.write('Hello!!!!')


a = (x for x in range(1, 1000000))
for i in a:
    i = i ** 2
    print(i)





def my_lazy_gen():
    for x in range(100000):
        yield x ** 2


for i in my_lazy_gen():
    print(i)
